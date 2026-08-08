class Phone:
    def __init__(self, brand, price, model, fn):
        # __init__就是构造函数
        # self相当于是this
        self.brand = brand
        self.price = price
        self.model = model
        self.fn = fn


# 封装华为手机
huawei = Phone('华为', 6999, 'mate80promax', lambda: print('我要打电话'))

print(huawei.__dict__)
huawei.fn()
