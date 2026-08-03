# 待合并的两个数组
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 方法1
for item in num_list2:
    # 将第二个数组中的内容遍历添加进数组1
    num_list1.append(item)

print(num_list1)

# 定义结果数组存储去重后的结果
result_list = []
# 进行数组去重
for num in num_list1:
    # 待合并的数组每个元素如果出现在结果数组了，则不进行追加
    if num not in result_list:
        result_list.append(num)

# 打印结果
print(result_list)

# 通过解构赋值的方式，拆解数组
wcy = ['我叫汪宸宇']
hyg = ['黄一个']
result_name = [*wcy,*hyg]
print(result_name)

# 通过+号进行连接，数据容器可以通过拼接的方式自动合并
love = ['我','爱','你']
name = ['薇','欧','拉']
print(love + name)