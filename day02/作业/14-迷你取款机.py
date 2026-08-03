# 简易取款机
money_base = 10000
menu = [
    '1. 查询余额',
    '2. 存款',
    '3. 取款',
    '4. 退出'
]

# 存款校验
def save_ok(m):
    return m > 0
# 取款校验，大于0且不能大于余额
def money_ok(m,balance):
    return 0 < m <= balance

while True:
    print('欢迎来到小汪银行')
    # 打印菜单
    for i in menu:
        print(i)

    print()
    # 接收用户输入
    user_control = input('请选择菜单:')

    match user_control:
        case '1':
            print(f"当前余额：{money_base}")
        case '2':
            user_input = int(input('请输入存款金额'))
            # 将存款金额调用合法性函数，进行检查
            if save_ok(user_input):
                # 如果输入合法，加钱
                money_base += user_input
        case '3':
            user_input = int(input('请输入取款金额'))
            # 取款金额传入合法性函数进行检查
            if money_ok(user_input,money_base):
                # 如果输入合法，扣钱
                money_base -= user_input
        case '4':
            break
