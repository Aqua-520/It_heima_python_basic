# for in的循环是一种轮训机制，从数据容器中依次取出数据进行遍历
def log_hyg():
    arr = [
        'hello',
        '我是黄一个',
        '考上东京大学美术学硕士',
        '走上人生巅峰'
    ]

    for item in arr:
        # 打印数组内容
        print(item, end='\n')
    else:
        print('循环结束')
log_hyg()