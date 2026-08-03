count = 5
while count > 0:
    username = input('请输入用户名')
    password = input('请输入密码')

    # 登录校验
    if username == 'admin' and password == '666888':
        print('登录成功')
        break
    elif username == 'zhangsan' and password == '123456':
        print('第二个账号登录成功')
        break
    else:
        count -= 1
        if count > 0:
            print(f'输入错误，请重试，还剩{count}次机会')
        else:
            print("错误次数已用尽，登录失败")