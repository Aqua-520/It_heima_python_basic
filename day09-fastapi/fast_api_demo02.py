# 创建被限定的对象
# 限定对象里面的属性类型
# 类似interface
import asyncio
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 创建api实例
# 可以给FastAPI类添加描述
app = FastAPI(title='FastAPI学习文档', description='小汪的测试学习用例', version='1.0.1')


# 创建类限定
class User(BaseModel):
    id: int = Field(description='用户id,唯一字段', examples=[1, 2, 3, 4, 5])
    name: str = Field(description='用户姓名', examples=['汪宸宇'], min_length=2, max_length=15)
    age: int | None = Field(default=None, description='用户年龄', gt=0, lt=100)


# 返回数据
# summary代表这个接口的描述,response_model接收一个类型,代表这个接口返回什么样的数据
@app.get('/', summary='获取黄一个的列表', response_model=list[User])
def get_user_info():
    temp_List = []
    for i in range(5):
        temp_List.append(User(id=i + 1, name=f'黄{i + 1}哥', age=18))
    return temp_List


# 定义耗时操作
async def async_mock():
    print('异步任务开始执行')
    # 外层函数执行到内层await就会跳出,等待同步任务执行完毕后回头依次取异步任务
    await asyncio.sleep(3)
    print('异步任务执行结束')


# 定义异步任务
@app.get('/test_async')
async def run_async_test():
    start = time.time()
    # 批量调用异步任务
    await asyncio.gather(
        async_mock(),
        async_mock(),
        async_mock()
    )
    end = time.time()
    return f'全部异步任务执行完毕: {end - start:.2f} 秒'
