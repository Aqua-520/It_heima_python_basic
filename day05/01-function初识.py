# 通过def定义，缩进表示归属关系
def hello_word():
    """
    打印一个 --- 用来区分代码片段用的
    :return:
    """
    # 函数可以无参数无返回值
    print('-' * 20,'hello_word','-' * 20)

hello_word()
hello_word()
hello_word()

# 输入参数
def leijia(num):
    """
    累加从1 到 num 入参的值，无返回值
    :param num:
    :return: None
    """
    total = 0
    while total < num:
        total += num
    print(total)

leijia(100)

# 有返回值
def zhazhiji(fruit):
    # 接收一个水果
    print('正在加工水果')

    return str(fruit + '汁')

result= zhazhiji('苹果')
print(result)

# 函数多个入参通过，分开
def jiehun(name1,name2):
    return f'{name1}和{name2}结婚了'

jiehun_result = jiehun('一个','小月')
print(jiehun_result)

# 多个返回值
def calculate_rectangle_perimeter_and_area(l,w):
    """
    计算长方形（正方形）的周长和面积
    :param l: 是长，单位cm
    :param w: 是宽，单位cm
    :return: 返回面积和周长
    """
    current_perimeter = (l + w) * 2
    current_area = l * w
    return current_perimeter,current_area

perimeter, area = calculate_rectangle_perimeter_and_area(25.3,20)
print(f'周长是：{perimeter}cm，面积是：{area}cm')