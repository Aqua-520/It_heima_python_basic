# 判断考试分数是否大于680分
# score = int(input('请输入您的考试成绩：'))
#
# if 750 <= score >= 680 :
#     print('欢迎来到清华大学或者北京大学')
# else:
#     print('滚去上大专吧废物')

# 验证账号密码，进行登录的操作
user = {
    "username":"admin",
    "password":"123456"
}

print('欢迎来到游乐场，请输入您的账号密码')
# 收集用户信息
inputUserInfo = input('请输入用户名：')
inputPassword = input('请输入您的密码：')

if inputUserInfo == user['username'] and inputPassword == user['password']:
    print('登录成功，欢迎来到提瓦特大陆')

# 用户名和密码错误一个都无法登录
if inputUserInfo != user['username'] or inputPassword != user['password']:
    print('用户名或密码输入错误，请重试')