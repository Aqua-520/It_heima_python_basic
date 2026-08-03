# 输入考试成绩判断层级
score = int(input('请输入成绩'))

if score > 100 or score < 0:
    print('请输入真正的分数')
else:
    if score >= 85:
        print('你好优秀')
    elif score >= 60:
        print('鸡哥')
    else:
        print('不及格')