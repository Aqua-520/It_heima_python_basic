class Animal:
    def speak(self):
        print('大叫')


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


def pleas_speak(obj: Animal):
    # 函数接收Animal类型的对象实例
    obj.speak()


pleas_speak(Cat())
# 多态指的是一个api提供接口,这里指的是一个接口函数
# 传入不同的对象调用相同名称的方法,会执行不同的逻辑
# 这样的表现叫做多态
