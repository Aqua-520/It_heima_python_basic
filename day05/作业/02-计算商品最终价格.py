"""
1. 商品总金额
    - 遍历所有传入的商品元组，将每个商品的 价格 × 数量 累加求和。
2. 优惠券扣减
    - 使用条件：商品总金额 ≥ 5000 元才可以使用优惠券。
    - 额度限制：优惠券金额不得超过商品总价（即不得让抵扣后金额为负数）。
    - 不满足条件时，优惠券不生效。
3. 积分抵扣
    - 使用条件：商品总金额 ≥ 5000 元才可以使用积分抵扣。
    - 兑换比例：100 积分 = 1 元，积分只能整百抵扣（即实际抵扣金额 = score // 100）。
    - 额度限制：积分抵扣金额不得超过商品总价。
    - 不满足条件时，积分抵扣不生效。
4. 运费
    - 直接累加到最终金额上，无任何限制。
"""

def calc_total_price(product_list, freight = 0, **kwargs):
    """
    :param product_list: 商品列表   [{'name':'iphone17','price':8888.88,'num':1},{'name':'iphone17','price':8888.88,'num':2}]
    :param freight: 运费
    :param kwargs: 优惠信息(有就计算,没有就不计算) 优惠券或者是积分
    :return: 订单总金额
    """
    # 遍历商品价格,推导式写法
    original_price = sum(goods_item['price'] * goods_item['num'] for goods_item in product_list)
    # 优惠后价格
    current_price = original_price

    # 拿到原价
    # print(original_price)
    # 判断是否传入了优惠券信息
    if  'coupon' in kwargs:
        # 优惠券关键字在剩余参数中,则进行规则计算
        # 优惠券必须在购物车商品额度大于5000时使用,且不能超过商品价格,让价格变成负数
        if  original_price >= 5000 and kwargs['coupon'] <= original_price:
            # 满足条件,可以使用优惠券
            current_price -= kwargs['coupon']

    # 判断是否传入积分
    if  'points' in kwargs:
        # 额度限制：积分抵扣金额不得超过商品总价。
        if original_price >= 5000 and kwargs['points'] // 100 <= original_price:
            # 满足条件才能使用积分
            points_discount = kwargs['points'] // 100
            # 计算折扣后的价格
            current_price -= points_discount

    # 累加运费
    current_price += freight
    return current_price

# 购物车信息
shopping_cart_list = [
    {'name': 'iPhone 17', 'price': 8888.88, 'num': 1},
    {'name': '华为 Mate 70', 'price': 6999.00, 'num': 2},
    {'name': '小米 15 Pro', 'price': 4999.00, 'num': 1},
    {'name': '三星 S25 Ultra', 'price': 9699.00, 'num': 1},
    {'name': 'OPPO Find X8', 'price': 3999.00, 'num': 3}
]
# 待测试优惠信息
discount_info = {
    'coupon': 5000,      # 优惠券减500元
    'points': 20000       # 积分抵扣200元
}

# 传入商品对象
# 调用时候如果传入key = value的形式,会被**的参数组合成dict
total_price_result = calc_total_price(shopping_cart_list,**discount_info,freight=30000)
print('最终商品应付价格为:')
print(total_price_result)