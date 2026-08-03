# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

# 讲以上数组解构合并
merge_list1 = [*list1,*list2,*list3]

# 定义结果列表，将数组进行去重
result_list1 = []

# 循环进行去重
for item in merge_list1:
    # 如果元素不在结果列表中，则执行添加操作
    if item not in result_list1:
        result_list1.append(item)

# 打印结果1的数组
result_list1.sort()
print(result_list1)

# 将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
result_list2 = [i ** 2 for i in list4 if i % 2 == 0 and i % 5 == 0]
print(result_list2)

# 将如下列表中的正数提取出来，封装为一个新的列表。
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10,
         -11, 16, 54, -14, 36, -16, 87, -39]

result_list3 = [x for x in list5 if x > 0]
result_list3.sort()
print(result_list3)