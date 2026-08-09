"""
基于面向对象的编程思想完成如下系统开发
- 需求：某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
  - 核心功能：
    - 会员登录：会员通过账号和密码登录系统
    - 借书：会员可以借阅库存中有余量的图书，输入图书的编号后，就可以借阅图书 (借阅前, 先将所有图书信息展示出来)
    - 还书：会员可以归还借阅的图书，输入图书编号后，就可以归还该图书 (还书前, 先将当前已借阅的图书信息展示出来)
    - 查看我的借阅：展示当前会员已经借阅的图书列表，展示出书籍的编号、书名
  - 借阅规则：
    - 普通会员最多可借3本
    - VIP会员最多可借 6+VIP等级 本 （VIP等级，默认为1）
  - 注意：
    - 登录成功（卡号和密码均正确）后，才可以访问该系统
    - 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
"""


# 生产单本书的工厂
class Book:
    def __init__(self, book_id, title, author, total_num):
        # 书籍id
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def __str__(self):
        # 紧凑单行格式,批量打印书籍时形成清爽列表,避免大量空行
        return (f"📚 [{self.book_id}] 📖《{self.title}》"
                f"  ✍️ {self.author}"
                f"  📊 总{self.total_num}本"
                f"  ✅ 可借{self.__available_num}本")

    # 借书
    def decrease_stock(self):
        # 直接扣减一本书
        if self.__available_num <= 0:
            return False
        # 通过库存校验则扣减一本书
        self.__available_num -= 1
        return True

    # 还书
    def increase_stock(self):
        self.__available_num += 1
