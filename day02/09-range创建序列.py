# for循环可以通过range函数来生成一个指定范围和步长的整数序列
# 算1 - 100 之间所有奇数累加和

total = 0
# range(start,end,step)
for item in range(1,101,2):
    # 当传递两个以上参数时，第二个为end，但是取不到end，所以为101
    total += item
else:
    print(f'累加和是：{total}')


sum = 0
# range(start,end,step)
for item in range(100,501,3):
    # 当传递两个以上参数时，第二个为end，但是取不到end，所以为101
    sum += item
else:
    print(f'累加和是：{sum}')