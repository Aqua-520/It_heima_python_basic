num1 = 10
num2 = 20

# 直接采用,的方式进行两个变量值交换
num1,num2 = num2,num1

# 结果20,10 交换完毕
print(num1,num2)

def switchNum(a,b):
    c = a
    a = b
    b = c
    return a,b
num1,num2 = switchNum(num1,num2)
print(num1,num2)