import os
import json
from typing import Any

import fastapi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel, Field

from day08.自己编的作业.文件读写 import content

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
    with open(assets_path['home_page'], 'r', encoding='utf-8') as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)


# 定义书本类
class Book(BaseModel):
    id: str
    title: str
    author: str
    publisher: str
    total_pages: int
    price: float


# 2. 查询全部书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档 【逻辑： 加载 data/books.json 中的数据, 组装并返回】
@app.get('/api/books')
def get_book_list():
    # 先判断文件是否存在
    if not os.path.exists(assets_path['book_list']):
        # 不存在报错
        return ResponseModel(code=404, message='找不到图书列表资源', data=None)
    # 过了if则执行查询操作
    with open(assets_path['book_list'], 'r', encoding='utf-8') as file:
        content = json.load(file)
        print(f'当前图书列表:{content}')
        temp_list = []
        # content进行对象化封装
        for item in content:
            temp_list = Book(item['id'], item['title'], item['author'], item['publisher'], item['total_pages'],
                             item['price'])

        return ResponseModel(code=200, message='查询图书列表成功', data=temp_list)


# 3. 新增书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档  【逻辑： 加载 data/books.json 中的现有数据, 将新的数据放在列表尾部, 然后再存入文件中】


# 4. 删除书籍 --> 请求参数、路径、请求方式、响应数据 ， 参照接口文档 【逻辑： 加载 data/books.json 中的现有数据, 找到要删除的这本书籍, 从列表中删除掉, 然后再存入文件中】


# 5. 启动FastAPI服务
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
