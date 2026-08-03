while True:
    # 用户输入用户名和密码
    username = input('请输入用户名')
    password = input('请输入密码')

    # 用户名密码不允许为空
    if username == '' or password == '':
        print('用户名或密码不允许为空')
        continue
    if username == 'admin' and password == '111111':
        print('欢迎来到小汪的世界')
        break
    elif username == '黄' and password == '黄一个牛逼':
        print('小黄太牛逼了')
        break
    else:
        print('用户名或密码错误，请重试')