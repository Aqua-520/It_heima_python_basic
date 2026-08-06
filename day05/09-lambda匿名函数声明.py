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

print(f"1 + 2的结果是:{calc_data(1,2,lambda arg1,arg2 : arg1 + arg2)}")
print(f"1 - 2的结果是:{calc_data(1,2,lambda arg1,arg2 : arg1 - arg2)}")
print(f"1 * 2的结果是:{calc_data(1,2,lambda arg1,arg2 : arg1 * arg2)}")
print(f"1 / 2的结果是:{calc_data(1,2,lambda arg1,arg2 : arg1 / arg2)}")

# 通过lambda关键字声明匿名函数
hello = lambda : print('hello,我是lambda声明的匿名函数')
# 调用匿名函数
hello()

# 声明带参数的匿名函数
fn2 = lambda string : print(f'我是带参数的lambda匿名函数,参数内容是:{string}')
fn2(
    '我好想打舞萌,上w6,变成美丽小女孩'
)