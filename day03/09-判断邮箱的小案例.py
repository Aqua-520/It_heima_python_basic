# 判断传入的字符串只能有一个@，和大于1个的.才行

user_email = input('请输入邮箱')

if user_email.count('@') and '.' in user_email:
    print('邮箱输入正确')
else:
    print('邮箱输入错无')