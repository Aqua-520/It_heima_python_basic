# 对字符串进行切片操作

id_card = '110230200109070056'

# 截取身份证的生日和性别
birth = id_card[6:-4:]
print(birth)

# 截取性别
sex = '女' if int(id_card[-2::-1]) % 2 == 0 else '男'
print(sex)