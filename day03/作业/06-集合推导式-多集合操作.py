# 【题目】
# 已知四个课外活动小组的成员名单：
# calligraphy_set = {"王林", "曾牛", "天运子", "韩立", "厉飞雨", "紫灵", "徐立国"}
# painting_set    = {"张铁", "王林", "曾牛", "王蝉", "韩立", "厉飞雨", "云露", "李化元"}
# music_set       = {"许木", "红蝶", "韩立", "天运子", "厉飞雨", "曾牛", "虎咆"}
# sports_set      = {"遁天", "天运子", "韩立", "姜老道", "紫灵", "云露", "虎咆"}
#
# 请完成以下操作：
# 1. 找出同时参加了所有四个小组的学生（四重交集）
# 2. 找出参加了书法组，但既没有参加绘画组也没有参加音乐组的学生
# 3. 使用集合推导式找出参加了书法组，但没有参加体育组的学生
# 4. 求出所有参赛学生名单（四组并集），并统计总人数
# 5. 统计每位学生在四个小组中总共出现的次数, 并输出(形式为: xxx 参加了 xxx 个小组)


# 书法组
calligraphy_set = {"王林", "曾牛", "天运子", "韩立", "厉飞雨", "紫灵", "徐立国"}
# 绘画组
painting_set    = {"张铁", "王林", "曾牛", "王蝉", "韩立", "厉飞雨", "云露", "李化元"}
# 音乐组
music_set       = {"许木", "红蝶", "韩立", "天运子", "厉飞雨", "曾牛", "虎咆"}
# 体育组
sports_set      = {"遁天", "天运子", "韩立", "姜老道", "紫灵", "云露", "虎咆"}

# 查询四个组都参加了的学生
all_set = calligraphy_set.intersection(painting_set,music_set,sports_set)
print(all_set)

# 找出参加了书法组，但既没有参加绘画组也没有参加音乐组的学生
# 意思就是，参加了书法组，但是绘画组和音乐组没有的，就是求差集
result_set2 = calligraphy_set.difference(painting_set,music_set)
print(result_set2)

# 使用集合推导式找出参加了书法组，但没有参加体育组的学生
result_set3 = {i for i in calligraphy_set if not i in sports_set}
print(result_set3)

# 使用并集，将所有集合全部丢入新集合，集合自动去重
result_set4 = calligraphy_set.union(painting_set,music_set,sports_set)
# 循环遍历
total = 0
for i in result_set4:
    total += 1
# 其实直接打印新集合的长度就行
print(total)

# 5. 统计每位学生在四个小组中总共出现的次数, 并输出(形式为: xxx 参加了 xxx 个小组)
# 先将所有的集合转成list，进行重复，然后我们通过并集来当做参数，传入到count中，计算学生出现的次数
all_list = list(calligraphy_set) + list(painting_set) + list(music_set) + list(sports_set)
# print(all_list)

# 循环去重后的列表
for stu in result_set4:
    # 讲result_set4 传进此list的count中作为参数进行查询
    print(f'{stu} 参加了 {all_list.count(stu)} 个小组')