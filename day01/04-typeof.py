# 此章节使用type和isinstance两个函数来确定值的类型

x = 10
print(type(x))
x = 520.1314
print((type(x)))
x = False
print((type(x)))
x = 'coanima'
print((type(x)))

# 使用instance函数,返回某个值是否是某种类型
name = '黄一个无敌'
result = isinstance(name,str)
print(result)

# 赋值空类型
isNone = None
# NoneType属于全局唯一的实例对象,无法手动输入None来判断空值类型
print(isinstance(isNone,type(None)))

