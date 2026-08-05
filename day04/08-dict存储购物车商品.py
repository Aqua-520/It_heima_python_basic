
"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""

# 商品数据库
shopping_cart = {}
# 打印提示语
menu = """
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 修改购物车         #
#         3. 删除购物车         #
#         4. 查询购物车         #
#         5. 退出购物车         #
###############################
"""

print("welcome to 小汪的小铺 ~")

while True:
    # 打印提示语
    print(menu)

    # 收集用户操作
    user_input = input('请输入您需要操作的编号：').strip()

    # 分支判断
    match user_input:
        case '1':
            # 添加购物车
            goods_name = input('请输入您需要新增的商品名称：').strip()

            if goods_name in shopping_cart:
                # 如果在购物车存在，直接拦截
                print('您需要新增的商品已经存在于购物车当中了哟')
                continue

            # 写入购物车的操作
            price = int(input('请输入商品价格：'))
            count = int(input('请输入商品数量：'))
            shopping_cart[goods_name] = {
                "price":price,
                "count":count
            }

        case '2':
             goods_name = input('请输入您需要修改的商品名称：').strip()
             if goods_name not in shopping_cart:
                 # 如果在购物车存在，直接拦截
                 print('您需要修改的商品不存在于购物车')
                 continue

             # 您需要修改价格还是数量呢：
             print('1，修改该商品价格')
             print('2，修改该商品数量')

             price_or_count = int(input().strip())
             match price_or_count:
                 case 1:
                    price = int(input('请输入商品价格：').strip())
                    shopping_cart[goods_name]['price'] = price
                 case 2:
                    count = int(input('请输入商品数量：').strip())
                    shopping_cart[goods_name]['count'] = count
                 case _:
                     print('操作非法')

        case '3':
             goods_name = input('您需要删除哪一件商品呢：').strip()
             if goods_name not in shopping_cart:
                 # 如果需要删除的商品不存在，直接拦截
                 print('您需要删除的商品不存在于购物车')
                 continue

             del shopping_cart[goods_name]
             print('删除成功')
        case '4':
            # 打印购物车
            for goods_name, value in shopping_cart.items():
                print(f'商品名称：{goods_name}，价格是：{value["price"]}，数量是：{value["count"]}')

        case '5':
            print(
                '再见'
            )
            break
        case _:
            # 非法操作
            print('您的操作非法了')











