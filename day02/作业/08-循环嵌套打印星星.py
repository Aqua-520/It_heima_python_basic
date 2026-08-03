# 打印三角形星星
for x in range(1,6):
    for y in range(1, x + 1):
        print('*', end='\t')
    print()

print('-' * 50)
# 嵌套打印金字塔
for row in range(1,7):
    for column in range(1, row + 1):
        print(column,end='\t')
    else:
        print()

print('-' * 50)
# 打印国际象棋棋盘
# 8 * 8，八行八列，奇数以实心开头，偶数以空心开头
# for row in range(1,9):
#     for column in range(1,5):
#         if row % 2 == 0:
#             # 如果奇数行则空心开头■□
#             print('□',end='\t')
#             print('■',end='\t')
#         else:
#             print('■', end='\t')
#             print('□', end='\t')
#     else:
#         print()

for row in range(8):
    # 定义一个变量拼接值
    line = ''
    for col in range(8):
        # 行+列的奇数为□
        if (row + col) % 2 == 0:
            line += '■  '
        else:
            line += '□  '
    print(line)