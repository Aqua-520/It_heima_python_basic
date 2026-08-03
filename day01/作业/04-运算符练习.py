# 求梯形面积
from operator import and_


def get_tra_area():
    # input收集信息
    # 梯形面积为,上底加下底 * 高 / 2
    high = float(input('请输入梯形的高度'))
    up = float(input('请输入梯形的上底长度'))
    down = float(input('请输入下底长度'))

    area = (up + down) * high / 2
    return area
# print(f'梯形的面积是:{get_tra_area()}cm²')

# 求圆的周长，和面积
def get_circle_calc():
    # 周长 = 2 * π * 半径
    # 面积 = π * 半径 * 半径
    # 请输入圆的半径
    r = float(input('请输入圆的半径是多少'))
    perimeter = 2 * 3.14 * r
    area = 3.14 * r * r

    # 直接打印结果
    print(f'圆的面积是:{area:.2f}cm²，圆的周长是{perimeter:2f}cm')
    return
# 手动调用
# get_circle_calc()

# 算身体的BMI指数：体重kg / 身高m的平方
def calculate_bmi():
    # 获取用户的身高和体重
    w = float(input('请输入体重，单位kg'))
    h = float(input('请输入身高，单位m'))

    # 身高的平方，自己 * 自己
    result = w / h ** 2
    print('您的bmi是%.2f'% result)
    return
# calculate_bmi()

# 将输入的秒数，转化成小时，分钟，秒的格式进行输出
def sec_to_hms():
    # 请输入需要转换的秒数
    second = int(input('请输入要转换的秒数'))

    # 一个小时是3600秒，直接进行整除操作，自动省略小数
    hour = second // 3600
    # 计算分钟，先用总秒数对3600，一个小时的量取余数
    left_second = second % 3600
    # 将剩余的余数拿来对60做整除
    minute = left_second // 60
    # 还剩多少秒数为对60取余数，去掉那些分钟制，最后的值则为剩余秒数
    sec = left_second % 60
    # 打印结果
    print(f"当前还剩{hour}时，{minute}分，{sec}秒")
    return
# sec_to_hms()

# 计算苹果价格：需要输入单价，重量，总价
def get_apple_price_total():
    price = float(input('请输入苹果单价(元)'))
    w = float(input("请输入购买重量(斤)："))

    print(f'苹果单价 {price} 元，购买 {w} 斤，总价 {price * w:.2f} 元')
    return
# get_apple_price_total()

# 计算语文数学英语三科平均分进行输出
def get_average_score():
    math = float(input('请输入数学考试分数'))
    english = float(input('请输入英语考试分数'))
    Chinese = float(input('请输入语文考试分数'))
    print(f'您的总分是{math + english + Chinese}')
    print(f'平均分是{(math + english + Chinese) / 3:.2f}')
    return
# get_average_score()

# 计算用户输入一个整数，大于10 并且小于50，则输出true或者false
def check_num():
    num = int(input('请输入一个数'))
    if(num > 10 and num <= 50):
        return  True
    else:
        return False
# print(check_num())

# 表达式写法
def check_num2():
    num = int(input('请输入一个数'))
    return 10 <= num <= 50
# print(check_num2())

# 输入语文和数学成绩，只要有一科大于90分，返回true
def check_score():
    # 输入两个分数
    math = float(input('请输入数学考试分数'))
    chinese = float(input('请输入语文考试分数'))
    return math > 90 or chinese > 90
# print(check_score())

"""
    模拟成绩统计评优
"""
def studen_score():
    name = input('请输入姓名')
    # 姓名：王林，总分：192，平均分：96，是否评为优秀：True
    english = float(input('请输入英语考试分数'))
    chinese = float(input('请输入语文考试分数'))
    # 判断考试成绩
    # 总分
    total = english + chinese
    # 平均分
    average = total / 2
    # 是否优秀
    flag = english > 85 and chinese > 85 or total > 180
    print(f'姓名：{name}，总分：{total:.1f}，平均分：{average}，是否评为优秀：{flag}')
    return
studen_score()

