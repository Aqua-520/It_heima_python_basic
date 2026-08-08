# 定义一个类
class Person:
    pass


# 创建实例对象
huang = Person()

# 封装属性,在python中,给实例对象封装属性或者修改
# 和js一样,通过.
# 字典则是[]属性的方式进行封装

huang.name = '黄一个'
huang.age = 18

# 不加__dict打印的是内存地址:对象指的是在内存中开辟的空间
# __dict通过字典的形式进行显示里面的数据
print(huang.__dict__)

# 通过.的方式访问对象的属性或者方法,和js一样
print(huang.name)
