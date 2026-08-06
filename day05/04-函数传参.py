# 通过位置传参数
def print_info(name,age,gender,city):
    """
    接收用户输入的四个参数，进行打印
    :param name: 用户姓名
    :param age: 用户年龄
    :param gender: 用户性别
    :param city: 所在城市
    :return: 无
    """
    print(f"用户姓名：{name},年龄：{age},性别：{gender},所在城市：{city}")
    return None

# 通过位置进行传参
print_info('黄一个个',18,'女','冈山县高粱市')

# 通过关键字进行传参
print_info(name='黄二个',age=100,gender='男',city='重庆市')

# 组合写法
print_info('黄三个',52,city="东京",gender='真寻')

# 使用元组解包
params1 = ('黄四个',77,'男','北京')
print_info(*params1)

# 使用字典解包
# 字典底层使用关键字传参的方式进行解包
# key必须跟函数定义时的参数名保持一致
params2 = {
    "name":'黄五个',
    "age":99,
    "gender":"女",
    "city":"hawaii"
}
print_info(**params2)