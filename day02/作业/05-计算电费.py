# 第一档电费，2880度以下 电费单价0.4883元/度
# 第二档：2880-4800度，电费单价0.5383元/度
# 第三档：4800度以上，电费单价0.7883元/度

# 输入你的用电度数
total_kwh = float(input('请输入您的用电度数'))

# 非0判断
if total_kwh < 0:
    print('输入非法')
else:
    if total_kwh <= 2880:
        # 计算第一档电费
        part1 = total_kwh * 0.4883
        print(f'你的电费是:{part1:.2f}元')
    elif total_kwh <= 4800:
        # 第二档，算上第一档满的钱，度数减去2880等于第二档的电
        part2 = (total_kwh - 2880) * 0.5383
        price = part2 + 2880 * 0.4883
        print(f'你的电费是:{price:.2f}元')
    else:
        # 以上
        part3 = (total_kwh - 4800) * 0.7883
        price = part3 + 2880 * 0.4883 + (4800 - 2880) * 0.5383
        print(f'你的电费是:{price:.2f}元')