"""
    案例：图书管理系统
    1. 添加图书信息：根据提示录入图书名称、作者、价格、库存数量，录入完成保存到系统中。
    2. 修改图书信息：输入要修改的图书名称，然后再提示输入新的作者、价格、库存数量，输入完成后修改图书信息。
    3. 删除图书信息：输入要删除的图书名称，根据名称删除图书信息。
    4. 查询图书信息：输入要查询的图书名称，根据名称查询图书信息并输出。
    5. 列出所有图书：遍历所有图书信息并输出。
    6. 图书统计：统计图书总数、库存总量、总价值、价格最高和最低的图书信息。
    7. 退出系统。
"""
from operator import ifloordiv

menu = """
# # # # # # # # # # # # # # # # # # # # # # # 【图书管理系统菜单】 # # # # # # # # # # # # # # # # # #
#       1. 添加图书  2. 修改图书  3. 删除图书  4. 查询图书  5. 列出所有图书  6. 图书统计  7. 退出系统        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用图书管理系统 ~")

book_database = {
    "亲热天堂": {"author": "自来也", "price": 99, "stock": 5},
    "三体": {"author": "刘慈欣", "price": 68, "stock": 10},
    "活着": {"author": "余华", "price": 35, "stock": 15},
    "海贼王":{"author":'尾田荣一郎',"price":66.88,"stock":100}
}
# case6 的统计结果
book_statistics = {
    "total_book_count": 0,        # 图书总册数（所有图书）
    "total_stock_count": 0,       # 当前库存总量
    "total_value": 0.0,           # 图书总价值
    "max_price_book": None,       # 价格最高图书完整信息（字典/图书对象）
    "min_price_book": None        # 价格最低图书完整信息（字典/图书对象）
}

# 判断某本书是否存在于数据库当中
def is_book_in_book_database(bookname):
    # 根据bookname进行查询
    flag =True if bookname in book_database else False
    return flag


while True:
    print(menu)

    # 输入用户参数
    user_input = input('请输入您需要继续的操作：').strip()

    match user_input:
        case '1':
            # 添加图书
            bookname = input('请输入您要新增的书籍：')
            if not is_book_in_book_database(bookname):
                # 如果书不存在于数据库，则可以执行写入操作
                author = input('请输入此书的作者：')
                price = float(input('请输入此书的价格：'))
                stock = int(input('请输入此书的库存：'))
                # 写入数据库
                book_database[bookname] = {
                    "author": "自来也",
                    "price": 99,
                    "stock": 5
                }
            else:
                # 如果已经存在于数据库，告知用户
                print('此书已经在数据库有记录了，不能新增哦')
        case '2':
            # 修改图书
            bookname = input('请输入您要修改的书籍：')
            if is_book_in_book_database(bookname):
                # 如果书不存在于数据库，则可以执行写入操作
                author = input('请输入此书的作者：')
                price = float(input('请输入此书的价格：'))
                stock = int(input('请输入此书的库存：'))
                # 写入数据库
                book_database[bookname] = {
                    "author": author,
                    "price": price,
                    "stock": stock
                }
            else:
                print('您想修改的书不存在于数据库中，请先做新增操作')
        case '3':
            # 删除图书
            bookname = input('请输入您要修改的书籍：')
            if is_book_in_book_database(bookname):
                del book_database[bookname]
                print('图书删除成功')
            else:
                print('您想修改的书不存在于数据库中，请先做新增操作')
        case '4':
            # 查询图书
            bookname = input('请输入您要查询的书籍：')
            if is_book_in_book_database(bookname):
                book = book_database[bookname]
                print(f"书名：{bookname}")
                print(f"作者：{book['author']}")
                print(f"价格：{book['price']}")
                print(f"库存：{book['stock']}")
            else:
                print(f'未找到图书《{bookname}》')
        case '5':
            # 列出所有图书
            print('书名 \t 作者\t价格\t库存')
            for name, book in book_database.items():
                print(f"{name} \t {book['author']}\t{book['price']}\t{book['stock']}")
        case '6':
            if not book_database:
                print("当前数据库中无图书数据！")
                continue
            # 图书统计：统计图书总数、库存总量、总价值、价格最高和最低的图书信息。
            # 一共有几种书，直接用长度即可
            book_statistics["total_book_count"] = len(book_database)
            # 通过循环求所有书加起来的库存和价格
            total_stock_count = 0
            total_value = 0.0

            # minPrice
            # 初始化最高/最低价格的图书（记录书名和详情）
            max_price_name = None
            max_price_info = None
            min_price_name = None
            min_price_info = None
            for book_name,params in book_database.items():
                # params是商品参数，拿到stock
                total_stock_count += params['stock']
                total_value += params['price'] * params['stock']
                # 对比min_price_book[-1]的价格
                if max_price_info is None or params['price'] > max_price_info['price']:
                    max_price_name = book_name
                    max_price_info = params

                if min_price_name is None or params['price'] < min_price_info['price']:
                    min_price_name = book_name
                    min_price_info = params
            # 循环筛选结束
            book_statistics["min_price_book"] = (min_price_name,min_price_info)
            book_statistics["max_price_book"] = (max_price_name,max_price_info)
            book_statistics["total_stock_count"] = total_stock_count
            book_statistics["total_value"] = total_value


            # ========== 更简洁的写法（仅作学习参考，原逻辑保持不变）==========
            # 库存总量、总价值：一行 sum() 搞定
            # book_statistics["total_stock_count"] = sum(b['stock'] for b in book_database.values())
            # book_statistics["total_value"] = sum(b['price'] * b['stock'] for b in book_database.values())
            # 找价格最高/最低那本书：max()/min() + key=lambda 一行搞定
            # max_name, max_info = max(book_database.items(), key=lambda x: x[1]['price'])
            # min_name, min_info = min(book_database.items(), key=lambda x: x[1]['price'])
            # =============================================================

            print("========== 图书统计 ==========")
            print(f"图书种类数\t: {book_statistics['total_book_count']}")
            print(f"库存总量\t: {book_statistics['total_stock_count']}")
            print(f"图书总价值\t: {book_statistics['total_value']}")
            print(f"价格最高\t: 《{max_price_name}》  作者 {max_price_info['author']}  价格 {max_price_info['price']}")
            print(f"价格最低\t: 《{min_price_name}》  作者 {min_price_info['author']}  价格 {min_price_info['price']}")
            print("==============================")
        case '7':
            # 退出系统
            print('感想使用图书管理系统，再见')
            break
        case _:
            print('输入有误，请重新输入')