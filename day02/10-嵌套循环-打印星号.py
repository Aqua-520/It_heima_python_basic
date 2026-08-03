# 打印row行column列的星星

column = int(input('请输入您需要打印多少个星星'))
row = int(input('请输入您需要打印几行'))

for _ in range(row):
    for _ in range(column):
        print('*', end=' ')
    print()