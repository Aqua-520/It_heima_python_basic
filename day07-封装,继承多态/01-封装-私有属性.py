class Phone:
    def __init__(self, owner, model):
        self.model = model
        # 通过两条杠设置为私有属性
        self.__owner = owner

    # 私有方法：双下划线开头
    def __secret_greeting(self):
        print(f'悄悄打招呼：专属机主{self.__owner}，手机只为你待命✨')

    # 方法
    def run(self):
        # 类内部调用私有方法
        self.__secret_greeting()
        print(f'{self.model}正在开机,欢迎来到苹果的世界')


iphone17promax = Phone('汪宸宇', '17promax')

print(iphone17promax.model)
# 私有属性无法访问,解释器底层进行了改名,所以没有该属性了
# 如果找到改名后的属性其实还是能拿到数据的
# print(iphone17promax.__owner)

# 调用方法
iphone17promax.run()

# 拿到改名后的还是可以调用
iphone17promax._Phone__secret_greeting()
