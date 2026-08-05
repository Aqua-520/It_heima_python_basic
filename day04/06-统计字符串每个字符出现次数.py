user_input = input('请输入一个字符串：')

# 定义空字典
result_dict = {}

# 循环统计字符串
for char in user_input:
    if char in result_dict:
        # 如果此字符作为key能在dict中找到，则自增1
        result_dict[char] += 1
    else:
        # 没找到则初始化为1
        result_dict[char] = 1

# 打印结果
for key,value in result_dict.items():
    print(f"字符:{key},在:{user_input}中出现了:{value}次")