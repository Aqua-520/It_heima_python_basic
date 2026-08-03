# 通过for循环进行99乘法表的打印
# 终止值为10是为了能取到第9行
for row in range(1,10,1):
    # 内层循环：控制每行的列数。第 row 行就打印 row 列，所以终止值写 row + 1（才能包含 row 本身）
    for column in range(1, row + 1, 1):
        print(f"{column} * {row} = {row * column}",end='\t')
    print()