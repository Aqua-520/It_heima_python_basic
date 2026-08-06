"""
给定学生列表，基于学生列表完成如下需求：
需求1：对于学生列表中的学生信息根据年龄进行升序排序
需求2：对于学生列表中的学生信息根据分数进行降序排序
需求3：对于学生列表中的学生信息先按照年龄升序，年龄相同再按照分数降序
需求4 ：过滤出年龄 >=18 岁的学生             [stu  for stu in students if stu['age'] >= 18]
需求5 ：过滤出年龄 <18 岁的学生              [stu  for stu in students if stu['age'] < 18]
需求6：过滤出性别为男的学生                  [stu  for stu in students if stu['sex'] < '男']
需求7：过滤出性别为 女的学生                 [stu  for stu in students if stu['sex'] < '女']
需求8：过滤出分数>90分的女学生               [stu  for stu in students if stu['score'] > 90]
需求9：过滤出年龄小于20 且分数>90 的女学生    [stu  for stu in students if stu['age'] < 20 and stu['score'] > 90 and stu['sex'] == '女' ]
"""

students_list = [
    {"name": "张伟", "age": 20, "sex": "男", "score": 88.5, "city": "北京"},
    {"name": "李娜", "age": 19, "sex": "女", "score": 92.0, "city": "上海"},
    {"name": "王强", "age": 21, "sex": "男", "score": 76.3, "city": "广州"},
    {"name": "刘洋", "age": 20, "sex": "女", "score": 95.5, "city": "深圳"},
    {"name": "陈静", "age": 18, "sex": "女", "score": 83.0, "city": "成都"},
    {"name": "赵磊", "age": 22, "sex": "男", "score": 67.8, "city": "武汉"},
    {"name": "周婷", "age": 19, "sex": "女", "score": 91.2, "city": "南京"},
    {"name": "吴迪", "age": 20, "sex": "男", "score": 79.6, "city": "西安"},
    {"name": "郑爽", "age": 21, "sex": "女", "score": 88.0, "city": "杭州"},
    {"name": "孙阳", "age": 20, "sex": "男", "score": 72.4, "city": "重庆"},
]

# 需求1：对于学生列表中的学生信息根据年龄进行升序排序
students_list.sort(key= lambda stu_obj : stu_obj['age'])
print('需求1：对于学生列表中的学生信息根据年龄进行升序排序')
for stu in students_list:
    print(stu)
print("-" * 50)


# 需求2：对于学生列表中的学生信息根据分数进行降序排序
students_list.sort(key= lambda stu_obj_item : stu_obj_item['score'],reverse=True)
print("需求2：对于学生列表中的学生信息根据分数进行降序排序")
for stu in students_list:
    print(stu)
print("-" * 50)


# 需求3：对于学生列表中的学生信息先按照年龄升序，年龄相同再按照分数降序
students_list.sort(key= lambda stu_obj_item : (stu_obj_item['age'],-stu_obj_item['score']))
print("需求3：对于学生列表中的学生信息先按照年龄升序，年龄相同再按照分数降序")
for stu in students_list:
    print(stu)
print("-" * 50)

# 自定义排序函数
def my_filter(arr,fn):
    # 推导式将符合规则的数堆入函数的比较结果,函数返回布尔类型,根据布尔类型判断当前循环的item要不要放入结果数组
    # 这个推导式拿到的是一个个学生对象,传入lambda的时候需要通过key来访问具体数值
    result_list = [item for item in arr if fn(item)]
    # 返回排序完成后的结果数组
    return result_list

# 需求4 ：过滤出年龄 >=18 岁的学生   [stu  for stu in students if stu['age'] >= 22]
print("需求4 ：过滤出年龄 >= 22 岁的学生")
# 返回一个筛选过后的全新list
result4 = my_filter(arr=students_list,fn=lambda current_item_obj : current_item_obj['age'] >= 22)
for stu_item in result4:
    print(stu_item)
print("-" * 50)

# 需求5 ：过滤出年龄 <18 岁的学生    [stu  for stu in students if stu['age'] < 18]
print("需求5 ：过滤出年龄 < 19 岁的学生")
# 返回一个筛选过后的全新list
result5 = my_filter(arr=students_list,fn=lambda current_item_obj : current_item_obj['age'] < 19)
for stu_item in result5:
    print(stu_item)
print("-" * 50)

#需求6：过滤出性别为男的学生        [stu  for stu in students if stu['sex'] < '男']
print("需求6：过滤出性别为男的学生")
result6 = my_filter(students_list,lambda current_obj : current_obj['sex'] == '男')
for item in result6:
    print(item)
print("-" * 50)

#需求7：过滤出性别为 女的学生        [stu  for stu in students if stu['sex'] < '女']
print("需求7：过滤出性别为 女的学生")
result7 = my_filter(students_list,lambda current_obj : current_obj['sex'] == '女')
for item in result7:
    print(item)
print("-" * 50)

# 需求8：过滤出分数>90分的女学生               [stu  for stu in students if stu['score'] > 90]
print("需求8：过滤出分数>90分的女学生")
result8 = my_filter(students_list,lambda current_obj : current_obj['score'] > 90)
for item in result8:
    print(item)
print("-" * 50)

# 需求9：过滤出年龄小于20 且分数>90 的女学生
print("需求9：过滤出年龄小于20 且分数>90 的女学生")
result9 = my_filter(students_list,lambda stu_obj_info : stu_obj_info['age'] < 20 and stu_obj_info['score'] > 90 and stu_obj_info['sex'] == '女')
for item in result9:
    print(item)