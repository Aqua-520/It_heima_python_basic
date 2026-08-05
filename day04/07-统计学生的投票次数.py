import random

stu_num = int(input('请输入参与投票的学生个人：'))

# 一共有四个景点
jd = (
    'tokyo',
    'chiba',
    'yokohama',
    'oosaka'
)

# 循环学生人数
result = {}
for stu in range(stu_num):
    # 随机出现下标
    index = random.randint(0,3)
    if jd[index] in result:
        result[jd[index]] += 1
    else:
        result[jd[index]] = 1

print(result)