# 使用while循环打印十次
def print_life():
    count = 1
    while count <= 10:
        print(f'人生苦短，我好难过。第{count}次执行')
        count += 1
    else:
        print('循环结束')

# print_life()

# 求1到100，所有偶数的累加和
def sum_even_100():
    # 定义循环变量
    x = 2
    # 累加变量
    total = 0
    while x <= 100:
        # 输出所有偶数
        print(x,end=' ')
        # 将偶数累加
        total += x
        # 循环变量自增步长为2
        x += 2
    else:
        # 空打印，输出换行
        print()
        print(f'循环完毕,总和为：{total}')

sum_even_100()
