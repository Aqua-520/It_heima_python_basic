# 请输入月份
month = int(input('请输入月份'))
# 数值规范校验
if month <=0 or month > 12:
    print('输入非法月份，请重试')
else:
    match month:
        case 3 | 4 | 5:
            print('春季')
        case 6 | 7 | 8:
            print('夏季')
        case 9 | 10 | 11:
            print('秋季')
        case 12 | 1 | 2:
            print('冬季')
