# 【题目】
# 已知若干学生的课程选课数据：
# students = (
#     ("S001", "王林", {"语文", "数学", "英语", "历史"}),
#     ("S002", "李慕婉", {"数学", "物理"}),
#     ("S003", "司徒南", {"语文", "英语", "历史"}),
#     ("S004", "柳眉", {"数学", "英语", "物理"}),
#     ("S005", "周佚", {"语文", "数学", "化学", "历史"}),
#     ("S006", "清水仙君", {"语文", "数学", "AI", "日语"}),
#     ("S007", "红蝶", {"英语", "数学", "日语"}),
#     ("S008", "徐立国", {"语文", "英语", "历史"}),
#     ("S009", "许立国", {"语文", "历史", "AI"}),
#     ("S010", "藤化元", {"语文", "英语", "化学", "韩语"})
# )
# hot_courses = {"数学", "英语", "物理"}
#
# 请依次完成以下操作（不使用函数）：
# 1. 使用元组解包遍历所有学生，输出每个学生的学号、姓名和所选课程
# 2. 求出所有学生选过的全部课程集合 all_courses
# 3. 计算每个学生的总学分（每门课 3 学分）, 并输出(形式: "xxx 选修了 xxx 课程, 总学分 xxx 分")
# 4. 找出所选课程中至少包含 2 门热门课程的学生
# 5. 找出选了"数学"但没选"物理"的学生姓名

students = (
    ("S001", "王林", {"语文", "数学", "英语", "历史"}),
    ("S002", "李慕婉", {"数学", "物理"}),
    ("S003", "司徒南", {"语文", "英语", "历史"}),
    ("S004", "柳眉", {"数学", "英语", "物理"}),
    ("S005", "周佚", {"语文", "数学", "化学", "历史"}),
    ("S006", "清水仙君", {"语文", "数学", "AI", "日语"}),
    ("S007", "红蝶", {"英语", "数学", "日语"}),
    ("S008", "徐立国", {"语文", "英语", "历史"}),
    ("S009", "许立国", {"语文", "历史", "AI"}),
    ("S010", "藤化元", {"语文", "英语", "化学", "韩语"})
)
hot_courses = {"数学", "英语", "物理"}

# 1. 使用元组解包遍历所有学生，输出每个学生的学号、姓名和所选课程
for stu in students:
    # 每一个stu是一个元组，进行解包
    stu_num,name,courses = stu

    # 字符串拼接
    course_str = '、'.join(courses)
    # print(stu_num,name,courses)
    print(f'学号{stu_num}，姓名：{name}，\t所选课程：{course_str}')

print('-'*50)
# 求出所有学生选过的全部课程集合 all_courses
# 定义空集合
all_courses = set()
# 循环遍历原来的二维元组
for item in students:
    # 解构item
    stu_num,name,course = item
    # course就是元组，调用元组的update方法，新值传入自动去重，保留没有重复的元素
    all_courses.update(course)

# 成功对所有的课程进行去重
print(all_courses)

print('-'*50)
# 3. 计算每个学生的总学分（每门课 3 学分）, 并输出(形式: "xxx 选修了 xxx 课程, 总学分 xxx 分")
for stu_tuple in students:
    stu_num,name,course_set = stu_tuple
    # 选修了xx课程
    couse_str = '、'.join(course_set)
    print(f"{name} 选修了 {couse_str} 课程, 总学分 {len(course_set) * 3} 分")

print('-'*50)
# 4. 找出所选课程中至少包含 2 门热门课程的学生
# 包含热门课程就是求所选课程中，对于热门课程的并集
for stu_tuple in students:
    stu_num,name,course_set = stu_tuple
    result =  course_set.intersection(hot_courses)
    if  len(result) >=2:
        print(f"{name} 修了 {result} 这些热门课程")

print('-'*50)
# 5. 找出选了"数学"但没选"物理"的学生姓名
for stu_num,name,course_set in students:
    if '数学' in course_set and '物理' not in course_set:
        print(f"选了数学但没选物理的学生有：{name}")