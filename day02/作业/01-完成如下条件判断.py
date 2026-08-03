# 根据用户输入的数字，判断基数还是偶数
num1 = int(input('请输入一个数字'))
if num1 % 2 == 0:
    print('是偶数')
else:
    print('是奇数')

# 判断是否成年
age = int(input('请输入年龄'))
if age >= 18:
    print('您是成年人')
else:
    print('您是小灯，未成年别来网吧')

# 判断是正数还是负数还是0
num2 = int(input('请输入一个数字'))
match num2:
    case _ if num2 > 0:
        print('是正数')
    case _ if num2 < 0:
        print('是负数')
    # 使用等值匹配
    case 0:
        print('是0')

# 判断分数是否及格
score = int(input('请输入分数'))
if score >= 60:
    print('及格了')
else:
    print('不及格')