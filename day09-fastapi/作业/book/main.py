import os
import json
from typing import Any
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# 文件路径
assets_path = {
    "home_page": "./static/index.html",
    "book_list": "./data/books.json"
}


# 确保 data 目录存在
# ==================== Pydantic数据模型 ====================
class ResponseModel(BaseModel):
    code: int = Field(description='响应状态码')
    message: str = Field(description='本轮响应的提示信息')
    data: Any = None


# 定义书本类
class Book(BaseModel):
    id: str
    title: str
    author: str
    publisher: str
    total_pages: int
    price: float


# ==================== 工具函数 ====================
def read_books_json() -> list[dict]:
    # 安全性校验，必须要有这个文件
    book_path = assets_path['book_list']
    if not os.path.exists(book_path):
        # 如果没有文件返回空列表
        return []

    # 找到了打开文件
    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            # 反序列化
            result_books = json.load(file)
            return result_books
    except Exception as e:
        print(e)
        return []


def write_books_json(book_list: list[dict]) -> bool:
    book_path = assets_path['book_list']
    # 写入列表
    try:
        # 安全校验，确保文件路径存在，没有则创建目录
        dir_path = os.path.dirname(book_path)
        # 2. 判断字符串不为空（防止直接传 "books.json" 导致切出空字符 ""）
        if dir_path:
            # 3. 真正到硬盘里检查：不存在就建，存在就忽略
            os.makedirs(dir_path, exist_ok=True)

        # 文件写入
        with open(book_path, 'w', encoding='utf-8') as file:
            # 列表排序
            new_list = sorted(book_list, key=lambda item: int(item['id'][1:]))
            json.dump(new_list, file, ensure_ascii=False, indent=4)

            return True
    except Exception as e:
        print(e)
        return False


# ==================== FastAPI 实例 ====================
app = FastAPI(title='图书信息增删改查接口', description='根据用户的请求,执行对应的操作逻辑', version='1.0.0')
# 挂载静态资源
if os.path.exists('./static'):
    app.mount('/static', StaticFiles(directory='./static'), name='static')


# ==================== API接口-操作函数(绑定路径与函数) ====================
# 1. 访问首页 ("static/index.html")
@app.get('/')
def get_home_page():
    # 判断文件是否存在
    if not os.path.exists(assets_path["home_page"]):
        # 不存在则报错
        return ResponseModel(code=404, message='您想查找的资源不存在', data=None)

    # 打开html文件将其作为HTMLResponse的类型返回
    with open(assets_path['home_page'], 'r', encoding='utf-8') as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)


# 2. 查询全部书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档 【逻辑： 加载 data/books.json 中的数据, 组装并返回】
@app.get('/api/books', summary='获取全部书籍')
def get_book_list():
    # 先判断文件是否存在
    # 直接通过打开文件的函数拿到结果
    book_list_result = read_books_json()
    if not book_list_result:
        # 没拿到数据则返回空
        return ResponseModel(code=404, message='找不到图书列表资源', data=None)
    return ResponseModel(code=200, message='查询图书列表成功', data=book_list_result)


# 3. 新增书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档  【逻辑： 加载 data/books.json 中的现有数据, 将新的数据放在列表尾部, 然后再存入文件中】
# 路径保持一致，但是使用post请求拿到请求体进行书籍的新增操作
@app.post('/api/books', summary='新增一本书籍')
def add_book(request: Book):
    # 先将数据库中的data加载出来，看看有没有id冲突
    book_list_result = read_books_json()

    # 收集用户传来的图书id
    temp_book_id = request.id
    # 把请求传来的id进行遍历对比看是否存在冲突
    for i in book_list_result:
        if i['id'] == temp_book_id:
            return ResponseModel(code=409, message='书本id存在冲突，必须为唯一标识', data=None)

    # 过了则进行新增操作，需要把用户的Book类型转换成dict类型才能新增
    # 使用BaseModel自带的方法，转换一下
    new_request = request.model_dump()

    # 将用户需要新增的传入书籍列表拼接
    book_list_result.append(new_request)

    # 把新的数据回写覆盖
    if write_books_json(book_list_result):
        # 返回新增数据
        return ResponseModel(
            code=200,
            message='书籍新增成功',
            data=new_request
        )
    return ResponseModel(
        code=500,
        message='书籍新增失败',
        data=None
    )


# 4. 删除书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档 【逻辑： 加载 data/books.json 中的现有数据, 找到要删除的这本书籍, 从列表中删除掉, 然后再存入文件中】
@app.delete('/api/books/{book_id}')
def delete_book_item(book_id: str):
    # 删除指定书籍
    print(f'要删除的书籍是{book_id}')

    # 拿到需要删除的id后，打开json文件
    book_list_result = read_books_json()

    # 对id做匹配
    is_find = False
    for i in range(len(book_list_result)):
        if book_list_result[i]['id'] == book_id:
            is_find = True
            # 因为每一个i是下标，remove需要传入完整的一整个dict才能做匹配，
            # 通过下标删除list当中的元素
            book_list_result.pop(i)
            break

    # 如果状态没修改则要删除的内容不存在
    if not is_find:
        return ResponseModel(code=404, message='未找到要删除的书籍', data=None)

    # 将新的json写入覆盖回去
    if write_books_json(book_list_result):
        # 返回删除成功的信息
        return ResponseModel(code=200, message='书籍删除成功', data=None)
    return ResponseModel(code=500, message='书籍删除失败', data=None)


# 5. 启动FastAPI服务
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
