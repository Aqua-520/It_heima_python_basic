# 内置方法，可以直接传入数组，进行求最大值，最小值，总计

# 循环输入五个数，通过list构造类创建空数组对象
arr = list()

for _ in range(5):
    arr.append(int(input(f'请输入第{_ + 1}个数')))

# 打印列表
print(arr)

# 最大值
print(f'最大值：{max(arr)}')
# 最小值
print(f'最小值：{min(arr)}')
# 总和
print(f'总和：{sum(arr)}')

# 平均数
print(f'平均数是：{sum(arr) / len(arr)}')