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


# 油车类
class FuelCar(Car):
    pass


# 电车类
class ElectricCar(Car):
    # 重新子类写一个重名方法,进行继承方法的覆盖
    def recharge(self):
        # 调用父类方法
        super().recharge()
        # 调用父类方法需要将实例对象传递过去,因为父类没有进行初始化生成
        Car.recharge(self)
        print(f'{self.brand} {self.model} 正在充电......')


# 生成电车对象
if __name__ == "__main__":
    tesla = ElectricCar('黑色', "特斯拉", "modely", "汪宸宇")
    print(tesla.color)
    tesla.recharge()
