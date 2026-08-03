# 在python中，列表跟js的数组差不多，唯一的区别是列表可以通过负索引来访问元素

list01 = [
    '黄一个',
    '好帅',
    '中国人会飞'
]

# 依次打印列表值
for index in range(3):
    # 通过自增索引的方式拿到元素的值
    print(list01[index])

print('-' * 50)
# 通过负数索引来拿到值
index = -1
while index >= -3:
    print(list01[index])
    index -= 1

print()
# 通过del关键字删除列表元素
del list01[2]
# 通过len函数拿到列表长度
i = 0
while i < len(list01):
    print(f"通过len函数进行的数组循环,当前元素：{list01[i]}")
    i += 1