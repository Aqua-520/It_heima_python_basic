import random

random_num = random.randint(1,100)
# print(ramdom_num)

count = 5
# 猜数字玩
while count > 0:
    print(f'当前还剩：{count}次机会')
    print()
    user_input = int(input('请输入您要猜的数字'))

    count -= 1
    # 逻辑判断
    if user_input == random_num:
        print('恭喜你，猜对了')
        break
    elif user_input < random_num:
        print('您猜的数字小了哦')
    elif user_input > random_num:
        print('您猜的数字大了哦')
else:
    print(f'五次机会用完了，正确数字是：{random_num}')