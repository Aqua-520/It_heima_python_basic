# 购物金额大于500 获得八折
# 300 - 500 块钱是九折
# 100 - 300 是95折
# 小于一百块则无折扣

# 请输入购物金额
price = int(input('请输入您的购物金额'))

if price < 0:
    print('金额不能小于0')
else:
    if price >= 500:
        print(f'八折，实际金额{price * 0.8}')
    elif price >= 300:
        print(f'九折，实际金额{price * 0.9}')
    elif price >= 100:
        print(f'九五折，实际金额{price * 0.95}')
    else:
        print('无折扣')