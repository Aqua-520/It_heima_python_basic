# 通过推导式语法来快速生成新的列表

# 在新的空列表当中，使用表达式语法，快速生成元素
result_list1 = [i**2 for i in range(1,21)]
print(result_list1)

# 推导式既可以加for，还可以加if
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]

# 使用推导式，基于已有的序列快速改造
result_list2 = [x ** 2 for x in num_list if x % 2 == 0]
print(result_list2)