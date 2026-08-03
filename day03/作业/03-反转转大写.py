# 循环输入五个字符串
# 每次输入将字符串反转
# 存入列表中
# 最后将列表大写，存入新列表，循环输出

# 临时容器
temp_list = []
for i in range(2):
    input_str = input('请输入英文字符串')
    # 字符串反转加转大写
    current = input_str[::-1].upper()
    # 字符串反转，添加进数组
    temp_list.append(current)

# 将数组从后往前排方法是修改原数组
temp_list.reverse()
for x in temp_list:
    print(x)