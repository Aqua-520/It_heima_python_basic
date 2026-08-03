# 在python中，所有的元素类型都是由类，进行创造出来的实例
# python是一门完整的面向对象的语言

arr_list = [1,2,3,4,5]

# append，末尾追加
arr_list.append('我是append')
print(arr_list)

# insert插入，在下标为1的位置插入元素，后面的元素自动位移
arr_list.insert(1,'我是insert插入物')
print(arr_list)

# remove，移除列表中第一个匹配到的值，必须存在于数组中
arr_list.remove(5)
print(arr_list)

# 不加参数默认弹出最后一个值
pop_result1 = arr_list.pop()
print(arr_list,pop_result1)

# 加了参数弹出指定位置
pop_result2 = arr_list.pop(1)
print(arr_list,pop_result2)

# 对数组反转
arr_list.reverse()
print(arr_list)

# 对数组排序,reverse参数默认为False，升序排序
arr_list.sort(reverse=False)
print(arr_list)

# 统计某个元素出现的次数
print(arr_list.count(4))