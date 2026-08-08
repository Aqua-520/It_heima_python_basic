class Phone:
    def __init__(self, brand, price, model):
        # __init__就是构造函数
        # self相当于是this
        self.brand = brand
        self.price = price
        self.model = model

    def call(self):
        print(f"{self.brand}{self.model}正在打电话")

    def stop(self):
        print(f"{self.brand}{self.model}电话打完了")

    def total_price(self, discount: float):
        # 计算优惠价格
        return self.price * discount


# 实例化
iphone = Phone('苹果', 9999, 'iphone17promax')
iphone.call()
iphone.stop()
print(iphone.total_price(0.9))

print('-' * 50)

huawei = Phone('华为', 12999, 'mate80promax')
huawei.call()
huawei.stop()
print(huawei.total_price(0.9))
