# 三角形的任意两边之和必须要大于第三边

a = int(input('请输入第一条边'))
b = int(input('请输入第二条边'))
c = int(input('请输入第三条边'))

# 排除0的情况
if a <=0 or b <= 0 or c <= 0:
    print('无法组成三角形，不能为0')
else:
    # 走到else，代表传入的边长度不为0
    if (a + b) > c and (b + c) > a and (a + c) > b:
        # 二次判断，能否构成三角形
        print('成功构成三角形')
        if a == b == c:
            # 三次判断，三角形为哪一种类型
            print('这是等边三角形')
        elif a == b or a == c or b == c:
            # 两个边相等则为等边三角形
            print('这是等边三角形')
        else:
            print('这是三条边不相等的三角形')
    else:
        print('三条边不满足于构成三角形的条件')