from fastapi import FastAPI

# 初始化app实例对象
api_demo = FastAPI()


# 定义函数映射
@api_demo.get('/')
def get_root():
    return '欢迎来到小汪的世界'


@api_demo.get('/userinfo')
def get_user_info():
    return {
        "name": "黄一个",
        "username": "黄二个",
        "age": "黄三个",
        "那么": "黄四个",
        "这么": "黄无个",
    }
