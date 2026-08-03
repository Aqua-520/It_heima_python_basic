# 输入密码和金额进行取款机扣款打印
# 正确字典格式
obj = {
    "balance": 10000,
    "password": "843708301"
}
# 收集用户信息
def qukuanji(password):
    if(password == obj['password']):
        print('密码输入正确')
        money = int(input('请输入取款金额'))
        obj['balance'] = obj['balance'] - money
        print(f'取款成功,余额为:{obj['balance']}')
        return
    else:
        print('密码错误,请重试')
        return

qukuanji(input('欢迎来到小汪银行,请输入密码'))