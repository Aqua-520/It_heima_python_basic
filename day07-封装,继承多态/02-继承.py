# 父类手机
class Phone:
    def __init__(self, owner):
        # 持有人为汪宸宇
        self.__owner = owner

    # 初始化功能
    def run(self):
        # 此私有属性会被设置成_Phone__owner 绑定到huawei实例身上
        # 当huawei通过指针拿到run的函数执行时,此类函数已经定义好了,所以_Phone__owner能正确拿到属性名
        print(f'{self.__owner}机主,正在启动设备')

    def __batery(self):
        print('正在切换cpu频率')


class Huawei(Phone):
    def __init__(self, owner, model_name):
        # 通过super调用父类的构造函数
        super().__init__(owner)
        self.model_name = model_name


# 实例化华为
huawei = Huawei('汪宸宇', "mate80pro")
print(huawei.model_name)

# 调用自己类身上没有的方法,会向上查找到父类,父类会调用自己身上的方法

huawei.run()
