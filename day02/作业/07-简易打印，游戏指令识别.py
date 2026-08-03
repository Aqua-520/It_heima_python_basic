# 输入上下左右，空格，j打印攻击
# esc退出

while True:
    # 指令
    gamer_control = input('请输入玩家指令：')
    match gamer_control:
        case 'w' | 'W':
            print('角色向上移动')
            continue
        case 's' | 'S':
            print('角色向下移动')
        case 'a' | 'A':
            print('角色向左移动')
        case 'd' | 'D':
            print('角色向右移动')
        case '':
            print('角色跳跃')
        case 'j' | 'J':
            print('角色攻击')
        case 'esc' | 'ESC':
            print('退出游戏')
            break
        case _:
            print('未知指令')  # 可选：处理无效输入