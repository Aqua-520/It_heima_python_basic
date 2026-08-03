# 如果当前年份，非整百年份，能被4整除，则为闰年
# 是整百年份的情况下，被400整除则为 闰年

# 请输入当前年份
year = int(input('请输入当前年份：'))

if year % 100 != 0 and year % 4 == 0:
    print('是闰年')
elif year % 100 == 0 and year % 400 == 0:
    print('是闰年')
else:
    print('是平年')