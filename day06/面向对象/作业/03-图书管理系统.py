"""
【需求说明】
1. 业务背景
   使用面向对象思想，开发一个图书管理系统，对图书信息进行统一管理，
   支持添加、修改、删除、查询单本、查询所有等功能。

3. 业务规则
   3.1 添加图书时：
       - 依次输入书名、作者、价格、库存
       - 书名不能重复（已存在则提示并返回）
       - 价格必须大于 0，库存必须大于等于 0，否则提示并返回
   3.2 修改图书时：
       - 输入要修改的书名
       - 若不存在则提示"未找到该图书"
       - 找到后依次输入新的作者、价格、库存，并更新
   3.3 删除图书时：
       - 输入要删除的书名
       - 若不存在则提示"未找到该图书"
   3.4 查询图书时：
       - 输入书名进行精确查询
   3.5 展示所有图书时：
       - 遍历 book_list，依次输出每一本图书的信息

4. 菜单
       1. 添加图书   2. 修改图书   3. 删除图书
       4. 查询指定图书  5. 查询所有图书  6. 退出系统
"""


# 2.1
# Book（图书类）
# - 实例属性：书名(title)、作者(author)、价格(price)、库存(stock)
# - 方法：
# *__init__：初始化方法，创建图书对象时设置所有属性
# *__str__：返回图书的字符串表示，格式为：
# "书名: xxx | 作者: xxx | 价格: xxx | 库存: xxx"
# *update_info：支持更新图书的作者、价格、库存（书名作为唯一标识不可修改）
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    # 格式输出
    def __str__(self):
        return f"书名: {self.title} | 作者: {self.author} | 价格: {self.price} | 库存: {self.stock}"

    # 书本更新方法
    def update_info(self, author, price, stock):
        # 支持更新图书的作者、价格、库存（书名作为唯一标识不可修改）
        self.author = author
        self.price = price
        self.stock = stock

# 2.2 BookSystem（图书管理系统类）
#     - 类属性：system_name（系统名称）、system_version（系统版本号）
#     - 实例属性：book_list（用于存放所有图书对象的列表）
#     - 方法：
#   * __init__：初始化方法，创建一个空的 book_list
#   * add_book：添加一本新图书
#   * update_book：修改指定图书的信息
#   * delete_book：删除指定图书
#   * query_book：查询指定图书
#   * list_books：展示所有图书
#   * run：显示菜单并循环接收用户操作

class BookSystem:
    system_name = '我是小汪的图书管理系统'
    system_version = '1.0.1'

    def __init__(self):
        # 初始化的图书管理列表
        self.book_list = []

    # 判断某本书是否存在于数据库中
    def book_is_in_database(self,name):
        for book in self.book_list:
            if book.title == name:
                return book

        return None
    # 收集书本信息的函数
    def get_book_info(self):
        author = input('请输入书本作者').strip()
        price = float(input('请输入书本价格').strip())
        # 价格必须大于 0，
        if price <= 0:
            print('书本价格需要大于0')
            return False

        stock = int(input('请输入书本库存').strip())
        # 库存必须大于等于 0
        if stock < 0:
            print('库存必须大于等于0')
            return False

        # 返回元组参数
        return author,price,stock


    # 新增
    def add_book(self):
        # 用户输入
        book_name = input('请输入需要新增的书籍名').strip()

        if self.book_is_in_database(book_name) is not None:
            # 如果不是空则不允许新增
            print('你想新增的书籍已经存在')
            return

        # 不存在则开始存储,收集书本信息
        # 调用收集信息的方法并解包
        author, price, stock = self.get_book_info()
        # 创建书本对象
        book_obj = Book(book_name,author,price,stock)
        # 将对象推入数组
        self.book_list.append(book_obj)

    def update_book
    def delete_book
    def query_book
    def list_books_log
    def run(self):
