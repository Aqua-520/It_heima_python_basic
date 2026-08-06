# 可以通过: 标注变量的类型
# 执行逻辑是在运行前,由编辑器来进行提醒.类似typescript

a: int = 10
name: str = '我被限定成了字符串类型'

# float或int类型
score: float | int = 88.9
isHungry: bool = True
is_null: None = None

# 限定数组里的子元素类型
stu_list: list[str] = ['黄一个','黄二哥']

# 限定元组的子元素类型
employee_list: tuple[str,...] = ('你好','我想吃疯狂星期四')
# 定长元组
point: tuple[int,int] = (100,200)

# 限定集合的子元素类型
lalala: set[str] = {'我是帅哥','我是大美女'}

# dict
dict1: dict[str,str | int | float] = {
    "我是key":100,
    "我是key2":"我是value",
    "我是key3":99.23
}

# 嵌套list加dict限定类型
user_info: list[dict[str,str]] = [
    {
        "username":'马化腾',
        "password":'abcd123123'
    }
]

# 函数类型注释
def output_num(a: int | float,b: bool) -> None:
    if b:
        print(a)

output_num(999,True)