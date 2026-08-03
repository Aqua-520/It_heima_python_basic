"""
    统计字符串 'akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd'
    字符串中有多少个a和k
"""

# 循环遍历字符串
str1 = 'akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd'

a_total = 0
k_total = 0
for item in str1:
    if item == 'a':
        a_total += 1
    elif item == 'k':
        k_total += 1
print(f'一共有{a_total}个a和{k_total}个k')