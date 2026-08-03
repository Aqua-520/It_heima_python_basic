# 接收身高体重，计算bmi
h = float(input('请输入身高，单位m'))
w = float(input('请输入体重，单位kg'))

# 边界保护
# 身高不能小于=0 体重不能小于=0
if h <= 0 or h > 2 or w <= 0 or w > 150:
    print('请输入正常数值，身高不能为0也不能超过2米')
    print('体重不能为0，也不能超过梁子')
else:
    # 计算bmi
    result = w / (h ** 2)
    if result < 18.5:
        print('偏瘦')
    elif 18.5 <= result < 24:
        print('正常')
    elif 24 <= result < 28:
        print('偏胖')
    else:
        print('你是梁子吗')