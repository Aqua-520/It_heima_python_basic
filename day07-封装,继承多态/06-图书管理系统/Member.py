from abc import ABC, abstractmethod


# 定义基类,专门拿来继承用
class Member(ABC):
    # 会员基类需要收集用户信息
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        # 当前会员借阅了哪些书籍,存放书籍信息的list
        self.borrow_list = []

    # 对抽象方法进行限定
    @abstractmethod
    def get_max_borrow_num(self) -> int:
        pass

    # 借阅书籍
    def borrow_book(self, book):
        # 先判断当前会员借的书籍有没有达到上限
        if len(self.borrow_list) >= self.get_max_borrow_num():
            print('您可以借阅的书籍已经达到最大数量')
            return False

        # 调用book身上的借书方法
        if book.decrease_stock():
            print('借书成功')
            # 将书本推入用户借书的list
            self.borrow_list.append(book)
            return True
        else:
            print('借书失败,库存不足')
            return False

    # 归还书籍的方法
    def return_book(self, book):
        # 需要系统传入书名做遍历匹配,或者是直接传入需要删除的对象进行匹配删除
        # 边界判断,如果要删除的书籍存在于会员已经借的列表中,则再执行删除
        if book in self.borrow_list:
            # 删除书籍
            self.borrow_list.remove(book)
            # 调用书籍对象身上的自增方法
            book.increase_stock()
        else:
            print('当前你想要归还的书籍,用户没有借哦')

    # 比对密码是否正确的方法
    def password_is_true(self, password):
        return self.__password == password

    # 展示会员当前借了哪些书籍
    def show_borrow_list(self):
        if len(self.borrow_list) == 0:
            print('当前用户还没有借阅任何书籍')
            return
        # 打印借书
        print('-' * 50)
        for item in self.borrow_list:
            print(item)

    #
