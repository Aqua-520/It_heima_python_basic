# match语法，后面跟变量，根据值进行case的路径匹配

num1 = float(input('请输入第一个数'))
num2 = float(input('请输入第二个数'))
op = input('请输入运算符')

match op:
    case '+':
        print((num1 + num2))
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/' if num2 != 0: # if 守卫，进行拦截。当匹配到此case时，if触发，如果第二个数为0则不执行此路径，走默认
        print(num1 / num2)
    case _:
        print('匹配失败')