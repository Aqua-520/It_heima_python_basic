def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# 定义一个函数,接收两个数值,并且第三个参数接收一个逻辑:函数进行补充
def calc_data(num1,num2,input_fn):
    """
    此函数接收两个值,通过第三个参数补充运算逻辑,返回第三个参数函数的运算结果
    :param num1: int
    :param num2: int
    :param input_fn: function
    :return: 返回第三个函数的运算结果
    """
    # 返回第三个参数函数的返回结果
    return input_fn(num1,num2)

print(f"1 + 2的结果是:{calc_data(1,2,add)}")
print(f"1 - 2的结果是:{calc_data(1,2,sub)}")
print(f"1 * 2的结果是:{calc_data(1,2,mul)}")
print(f"1 / 2的结果是:{calc_data(1,2,div)}")