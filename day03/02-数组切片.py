# 通过enumerate函数可以拿到数组的下标和元素
userlist = [
    '我会飞',
    '中午吃什么',
    'v50'
]
for index,item in enumerate(userlist):
    print(index,item)


# 对数组进行切片
num_list = [0,1,2,3,4,5]


# start不写从第一个开始截，end不写截取到最后，步长1
print(num_list[::1])
# 从下标1开始截取到下标3，不包含下标3
print(num_list[1:3:1])
# 从1号截取到下标-2
print(num_list[1:-2:])

# 将步长设置为负数，则从后往前截取
# 从最后一个截取到第一个
print(num_list[::-1])
print(num_list[:2:-1])

