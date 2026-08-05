# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# - 需求：根据提供的班级学生的选课情况，完成如下需求：
#   1. 找出同时选修了法语和艺术的学生
result1 = french_set & art_set
print(f'同时选修法语和艺术的学生是：{result1}')
print('-' * 50)

#   2. 找出同时选修了所有四门课程的学生
# 四重交集
result2 = football_set.intersection(basketball_set,french_set,art_set)
print(f'同时选修四门课的学生是：{result2}')
print('-' * 50)

#   3. 找出选修了足球, 但是没有选修篮球的学生
result3 = football_set.difference(basketball_set)
print(f'选修了足球, 但是没有选修篮球的学生是：{result3}')
print('-' * 50)

#   4. 统计每一个学生选修的课程数量
result_dict = {}
# 参加的学生名单，去重
all_student_list = basketball_set.union(french_set,art_set,football_set)
# 每个学生出现的次数
count_list = [*football_set,*french_set,*art_set,*basketball_set]

# 循环遍历学生
for stu in all_student_list:
    count = count_list.count(stu)
    # 存入字典
    result_dict[stu] = count

# 方式2：遍历【键 和 值】（最常用）
for name, num in result_dict.items():
    print(f"学生：{name}，选课门数：{num}")

# 获取姓王的学生姓名
result4 = []
for stu in all_student_list:
    if stu[0] == '王':
        result4.append(stu)
print(f'姓王的学生是：{result4}')
# 获取三个字
