# 元组就是无法增删改的list

tuple1 = ('黄一个','黄二哥','黄三个','黄三个','黄三个')

# 查找第一个黄三个出现的下标
three_index = tuple1.index('黄三个')

print(three_index)

# 也可以切片
print(tuple1[::3])
# 负数下标
print(tuple1[:-2:-1])

# 计算黄三个出现的次数
count = tuple1.count('黄三个')
print(count)