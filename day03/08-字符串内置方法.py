my_str = ' #Hello python python !!! '

# 通过find方法查找第一个符合子串的开始下标
index = my_str.find('python')
print(index)

# 从后往前查找，第一个符合子串规则的下标
index2 = my_str.rfind('python')
print(index2)

# 统计子串在字符串中出现的次数
py_count = my_str.count('python')
print(py_count)

# 将字符串转大写
upper_case = my_str.upper()
print(upper_case)

# 将字符串转小写
lower_case = my_str.lower()
print(lower_case)

# 将字符串按照指定间隔符号，拆分成子串，存储在list数组当中
sub_str_list = my_str.split(' ')
print(sub_str_list)

# 去除字符串开头和之后的间隔
new_str = my_str.strip()
print(new_str)

# 进行子串的替换,第三个参数，写1则代表只替换一次
replace_str = my_str.replace('python','script',1)
print(replace_str)

# 检查字符是否以某个字符开头，返回True or Flase
# 开头为空串，空格
startswith_str = my_str.startswith(' ')
print(startswith_str)

# 识别末尾是什么字符开头
end_swith_str = my_str.endswith('!')
print(end_swith_str)

file_name = 'wcy.pdf'
# 获取文件后缀名
ext_index = file_name.rfind('.')

# 通过正确的后缀名起始下标拿到后缀名
ext_name = file_name[ext_index::]
print(ext_name)