# if分支版
user_input = int(input('请输入一个整数'))

# 先判断是正数还是负数
if user_input < 0:
    # 小于0则为负数
    if user_input % 2 == 0:
        print('是负偶数')
    else:
        print('是负奇数')
elif user_input > 0:
    # 为正数
    if user_input % 2 == 0:
        print('是正偶数')
    else:
        print('是正奇数')
else:
    print('为0')

# 模式匹配版
match user_input:
    case 0:
        print('为零')
    case _ if user_input < 0:
        # 小于0则为负数
        if user_input % 2 == 0:
            print('是负偶数')
        else:
            print('是负奇数')
    case _ if user_input > 0:
        # 为正数
        if user_input % 2 == 0:
            print('是正偶数')
        else:
            print('是正奇数')