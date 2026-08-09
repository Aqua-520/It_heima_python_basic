# 汽车父类
class Car:
    def __init__(self, c_color, c_brand, c_model, owner):
        self.color = c_color
        self.brand = c_brand
        self.model = c_model
        # 私有属性 : 外界不能直接访问
        self.__owner = owner

    # 启动
    def start(self):
        print(f'{self.__owner}车主的 {self.brand} {self.model} 启动了......')

    # 停止
    def stop(self):
        print(f'{self.__owner}车主的 {self.brand} {self.model} 熄火了......')

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶...')

    # 补充燃料
    def recharge(self):
        print(f'{self.brand} {self.model} 正在补充燃料......')

    # 定义父Car的奔跑方法
    def running(self):
        print(f'180km超速飞奔')


# 定义父类(自动驾驶)
class SmartDriver:
    def __init__(self, company, level='L3'):
        self.company = company
        self.level = level

    def running(self):
        print(f'正在使用{self.company} {self.level}级别的自动驾驶技术开车.....')


# 电车类
class ElectricCar(Car, SmartDriver):
    # 初始化需要将此类的实例对象传入前面两个父类的构造函数当中进行属性的新增
    def __init__(self, c_color, c_brand, c_model, owner, company, level):
        # 传递实例对象,作为参数传过去
        Car.__init__(self, c_color, c_brand, c_model, owner)
        # 调用第二个实例对象的构造函数
        SmartDriver.__init__(self, company, level)


# 实例化电车
su = ElectricCar('粉色', '小米', 'su7', '汪宸宇', '华为', 'L3')
print(su.color)
# 调用方法
su.start()
# 在子类实例调用自己身上没有的方法时候,默认去第一个父类找,找不到再找第二个父类
su.running()
su.stop()

# 执行链
# 通过子类,类对象本身.__mro__属性,拿到执行链条
print(ElectricCar.__mro__)
