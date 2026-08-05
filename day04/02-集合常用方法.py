set1 = {'wcy','hyg','xyn','gszm'}
set2 = {'wcy','xjp','tlp'}

# 给2集合添加
set2.add('添加一个元素')
print(set2)
# 删除元素
set1.remove('gszm')
print(set1)

# pop弹出
pop_result = set1.pop()
print(pop_result)

# 求差集
difference_result = set1 - set2
print(difference_result)

# 交集
# intersection_result = set1.intersection(set2)
intersection_result = set1 & set2
print(intersection_result)

# 并集
union_result = set1 | set2
print(union_result)