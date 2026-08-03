x = 520
y = 1314

# 交换函数
def switchValue(a,b):
    temp = a
    a = b
    b = temp
    return a,b

x,y = switchValue(x,y)
print(x,y)

a = 100
b = 200
c = 300

# 使用快速语法交换相互的内存地址
c,a,b = a,b,c
print(a,b,c)