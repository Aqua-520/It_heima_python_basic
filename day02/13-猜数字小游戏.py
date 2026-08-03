import random

ramdom_num = random.randint(1,100)
# print(ramdom_num)

count = 1
# 猜数字玩
while True:
    print(f'当前第：{count}轮')
    print()
    user_input = int(input('请输入您要猜的数字'))

    count += 1
    # 逻辑判断
    if user_input == ramdom_num:
        print('恭喜你，猜对了')
        break
    elif user_input < ramdom_num:
        print('您猜的数字小了哦')
    elif user_input > ramdom_num:
        print('您猜的数字大了哦')