# 【题目】
# 请依次完成（不使用函数）：
# 每天打卡数据
monday    = ("王林", "李慕婉", "司徒南", "柳眉", "周佚", "清水仙君", "红蝶")
tuesday   = ("王林", "司徒南", "柳眉", "清水仙君", "红蝶", "徐立国", "许木")
wednesday = ("王林", "李慕婉", "司徒南", "周佚", "柳眉", "清水仙君", "红蝶", "徐立国")
thursday  = ("王林", "李慕婉", "周佚", "红蝶", "徐立国", "虎咆", "遁天")
friday    = ("司徒南", "柳眉", "清水仙君", "红蝶", "王林", "许木", "虎咆")

# 员工集合
all_employees = {"王林", "李慕婉", "司徒南", "柳眉", "周佚", "清水仙君", "红蝶", "徐立国", "许木", "虎咆", "遁天", "姜老道"}

# 1. 使用解包操作将五天的元组合并到一个大列表 all_records 中
all_records = [*monday,*tuesday,*wednesday,*thursday,*friday]
print(f"解包后的大列表：{all_records}")

# 2. 使用集合找出全勤员工（五重交集）
is_perfect_attendance = set(monday).intersection(tuesday,wednesday,thursday,friday)
print(f"全勤员工是：{is_perfect_attendance}")

# 3. 找出从未到岗的员工
# 算员工集合，对于出勤打卡的差集，我有你没有
absent_employees = all_employees.difference(monday,tuesday,wednesday,thursday,friday)
print(f'没到岗过的员工名称：{absent_employees}')

# 4. 统计每位员工的出勤天数
# 使用循环计算出勤天数
employee_result = []
for employee in all_employees:
    # 循环员工，作为大列表的count参数传递进去
    employee_result.append((employee,f'出勤天数：{all_records.count(employee)}'))

print(employee_result)

# 5. 使用列表推导式筛选出出勤天数 >= 4 的员工
frequent_employees = [emp for emp in employee_result if int(emp[-1][-1]) >= 4]
for i in frequent_employees:
    print(f'出勤天数大于四天的员工是：{i[0]}')

# 6. 找出只来了两天的员工姓名
two_days_employees = [emp for emp,days in employee_result if int(days[-1]) == 2]
for name in two_days_employees:
    print(f'只来了两天的员工是：{name}')
