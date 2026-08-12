"""
==========================================================
作业: 基于 FastAPI 开发"图书信息查询"API接口
==========================================================

【作业需求】
    使用 FastAPI 框架, 开发一个简单的"图书馆图书信息查询"API接口服务,
    用于查询图书馆中的图书列表信息。

【具体要求】
    1. 安装 FastAPI 与 uvicorn 依赖库
       - 命令: uv add fastapi uvicorn  (或 pip install fastapi uvicorn)

    2. 创建一个 FastAPI 实例对象, 并指定:
       - title       = "图书信息查询系统"
       - description = "一个简单的图书馆图书信息查询API"
       - version     = "1.0.0"

    3. 使用 Pydantic 模型定义图书数据结构 (类名: Book), 包含以下字段:
       - id      : int   图书ID
       - name    : str   图书名称
       - author  : str   作者
       - price   : float 价格
       - stock   : int   库存数量

    4. 开发以下 3 个 API 接口:
       (1) GET /
           - 功能: 根路径, 返回欢迎信息
           - 返回: {"message": "欢迎使用图书信息查询系统!"}

       (2) GET /books
           - 功能: 获取所有图书列表
           - summary: "获取所有图书列表"
           - response_model: list[Book]
           - 返回: 至少包含 3 本图书信息的列表, 图书信息定义在代码中即可
           - 提示: 在控制台打印 "获取图书列表..."

       (3) GET /books/count
           - 功能: 获取图书总数量
           - summary: "获取图书总数"
           - 返回: {"total": 图书数量}

    5. 通过代码方式启动 FastAPI 服务
       - host = "0.0.0.0"
       - port = 8000

    6. 启动后测试:
       - 在浏览器访问 http://localhost:8000/                   访问首页
       - 在浏览器访问 http://localhost:8000/books              查看图书列表
       - 在浏览器访问 http://localhost:8000/books/count        查看图书数量
       - 在浏览器访问 http://localhost:8000/docs               查看自动生成的接口文档
==========================================================
"""
from typing import Any
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
import uvicorn

# 创建实例
book_app = FastAPI(title='图书信息查询后台接口', description='根据用户的请求,返回相应的图书信息', version='1.0.0')


# 创建图书对象,pydantic对对象做类型限定
# 是为了返回的时候,返回的响应数据格式不出问题
class Book(BaseModel):
    # 限定类型
    id: int = Field(description='图书唯一标识,id', examples=[1, 2, 3])
    name: str = Field(description='图书名称', examples=['流浪地球', '战狼'], min_length=2)
    author: str = Field(description='作者', examples=['黄一个', '汪宸宇'], min_length=2)
    price: float = Field(description='图书价格', examples=[29.9, 100.0], gt=0)
    stock: int = Field(description='库存数量', examples=[10], gt=0)


# 定义一个响应对象
class ResponseModel(BaseModel):
    code: int = Field(description='状态码')
    message: str = Field(description='返回消息')
    data: Any = None


# 写个死的图书列表
book_list: list[Book] = [
    # 科幻文学
    Book(id=1, name="三体", author="刘慈欣", price=89.0, stock=50),
    Book(id=2, name="流浪地球", author="刘慈欣", price=45.0, stock=20),
    Book(id=3, name="银河帝国", author="阿西莫夫", price=128.0, stock=15),
    Book(id=4, name="沙丘", author="弗兰克·赫伯特", price=68.0, stock=30),

    # 当代名著
    Book(id=5, name="活着", author="余华", price=35.0, stock=45),
    Book(id=6, name="百年孤独", author="马尔克斯", price=55.0, stock=25),
    Book(id=7, name="平凡的世界", author="路遥", price=108.0, stock=18),
    Book(id=8, name="围城", author="钱钟书", price=39.5, stock=12),

    # 计算机与技术
    Book(id=9, name="Python编程：从入门到实践", author="埃里克·马瑟斯", price=89.0, stock=60),
    Book(id=10, name="算法导论", author="科曼", price=128.0, stock=10),

    # 心理学与社科
    Book(id=11, name="蛤蟆先生去看心理医生", author="罗伯特·戴博德", price=38.0, stock=40),
    Book(id=12, name="被讨厌的勇气", author="岸见一郎", price=42.0, stock=35),
]


# 定义接口
@book_app.get('/')
def welcome_message():
    return {
        "message": "欢迎来到小汪的图书管理系统"
    }


# 返回总共有几种图书种类
@book_app.get('/books/count', summary='返回总共有多少种书', response_model=ResponseModel)
def get_book_type_count():
    print('获取图书种类数量')
    return ResponseModel(
        code=200,
        message='返回图书分类总数',
        data=len(book_list)
    )


# 定义图书查询接口,根据传入的查询参数进行分割
@book_app.get('/books', summary='基于查询参数实现相对应的操作', response_model=ResponseModel)
def get_book_list(limit: int = Query(None, description='限制图书返回长度,不传返回全部')):
    print('获取图书列表')
    if limit is not None:
        # 对象封装
        return ResponseModel(
            code=200,
            message='返回指定数量的图书查询结果',
            data=book_list[:limit]
        )

    # 不传返回全部
    return ResponseModel(
        code=200,
        message='返回全部的图书查询结果',
        data=book_list
    )


# 通过uvicorn进行托管,监听端口
if __name__ == "__main__":
    uvicorn.run(book_app, port=1234)
