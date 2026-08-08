class Animal:
    leg = 4
    tax_rate = 0.1

    def __init__(self, name):
        self.name = name


dog = Animal('狗')
cat = Animal('猫')

# 通过类访问类方法
print(Animal.leg)
print(Animal.tax_rate)

# 通过实力对象向上查找
print(dog.leg)
print(cat.leg)

# 给实例对象新增属于自己的leg
dog.leg = 8
print(dog.leg)
# 原来的还是4,因为dog身上新增了leg属性
print(Animal.leg)
