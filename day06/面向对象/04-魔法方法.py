class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义魔法方法
    def __str__(self):
        # 在实例对象被直接被打印的时候,会执行__str__的return返回结果,不直接打印内存地址
        return f"我是str魔法方法,当前实例的属性是{self.name},{self.age}"

    # def __repr__(self):
    #     # 如果__str没定义,则使用repr的返回结果
    #     return 'repr的返回结果被调用了'

    # 比较方法
    def __eq__(self, other):
        # self 赋值为等号左边的对象,other接收等号右边的对象
        # 自定义比较规则,因为对象不能直接进行比较,比较内存地址没有意义
        return self.age == other.age

    def __lt__(self, other):
        # 也就是如果定义了gt则先使用gt, 没定义则将lt传入的对象进行镜像转换
        # < 左边的是self,我使用大于比较的时候,也就是说 self是hyg
        # other为wcy
        return self.age < other.age


wcy = Person('汪大帅比', 18)
print(wcy)

print('-' * 50)

hyg = Person('黄一个', 18)
print(hyg == wcy)

# < 号
print(wcy > hyg)
