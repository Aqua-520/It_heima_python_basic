# 图书信息管理系统class
# 图书系统需要管理用户信息,和图书信息两种
# 导入书本类和会员类
from Book import Book
from Member import Member
from NormalMember import NormalMember
from VipMember import VipMember
import json


# 定义图书管理系统
class LibrarySystem:
    message = '图书信息管理系统'
    version = '1.0.1'

    # 构造函数
    def __init__(self, mock=True):
        # 当前登录用户初始化为none
        self.current_member: Member | None = None
        # 进行mock数据初始化操作
        if mock:
            book_dict, member_dict = self.__mock_fn()
            # 初始化,直接写死图书信息和会员信息
            self.book_dict = book_dict
            self.member_dict = member_dict
        else:
            self.book_dict = {}
            self.member_dict = {}

    # 初始化函数
    def __mock_fn(self):
        # 图书字典
        # book_dict: dict[str, Book] = {
        #     # 直接用book类创建了书籍保存进了图书管理系统
        #     '1001': Book('1001', 'Python 教程', 'Python', 5),
        #     '1002': Book('1002', 'C++ 教程', 'C++', 3),
        #     '1003': Book('1003', 'Java 教程', 'Java', 2),
        #     '1004': Book('1004', 'C 教程', 'C', 1),
        #     '1005': Book('1005', 'JavaScript 教程', 'JavaScript', 4),
        # }
        # member_dict: dict[str, Member] = {
        #     # 这里直接用类创建对象进行保存了
        #     'N001': NormalMember(member_id='N001', name='张三', password='668001'),
        #     'N002': NormalMember(member_id='N002', name='李四', password='668002'),
        #     'N003': NormalMember(member_id='N003', name='王五', password='668003'),
        #     'V001': VipMember(member_id='V001', name='赵六', password='669001', vip_level=1),
        #     'V002': VipMember(member_id='V002', name='孙七', password='669002', vip_level=2),
        #     'V003': VipMember(member_id='V003', name='周八', password='669003', vip_level=3),
        #     'V004': VipMember(member_id='V004', name='吴九', password='669004', vip_level=4),
        # }
        """
        通过文件读写方式来进行数据导入
        :return: dict 数据
        """
        book_dict = {}
        member_dict = {}

        # book的书籍导入
        with open('./data/books.json', 'r', encoding='utf-8') as file:
            # 获取图书列表
            temp_book_list = json.load(file)
            # 组装字典
            for book_item in temp_book_list:
                book_dict[book_item['编号']] = Book(book_item['编号'], book_item['标题'], book_item['作者'],
                                                    book_item['数量'])

        # 会员信息导入
        with open('./data/members.json', 'r', encoding='utf-8') as file:
            # 获取会员信息
            temp_member_list = json.load(file)

            for member_item in temp_member_list:
                # if判断是哪个会员
                if member_item['id'].startswith('N'):
                    member_dict[member_item['id']] = NormalMember(
                        member_item['id'], member_item['name'], member_item['password'])
                elif member_item['id'].startswith('V'):
                    member_dict[member_item['id']] = VipMember(
                        member_item['id'], member_item['name'], member_item['password'], member_item["level"])

        return book_dict, member_dict

    #  1. 借阅图书  2. 归还图书  3. 查看用户借阅   4. 退出系统
    # 借阅图书
    def handle_borrow_book(self):
        # 先展示当前的书籍库存
        self.show_book_database()
        # 需要收集图书id,从图书字典中拿到图书对象
        book_id = input('请输入您想借阅的图书id:')
        # 判断是否存在于字典
        if book_id not in self.book_dict:
            # 如果不存在,则提示
            print('您想借阅的书籍本系统没有哦,请输入别的书籍')
            return
            # 如果存在于字典,将图书对象拿到
        book_obj = self.book_dict[book_id]
        # 通过用户对象来执行借取书籍的方法
        # 当前用户对象执行借阅书籍的操作,类似于系统找出书籍,丢给想借阅的人,然后由他来保存一份书籍信息
        self.current_member.borrow_book(book_obj)

    # 归还书籍
    def handle_return_book(self):
        # 打印一下用户现在身上拥有的图书信息列表
        self.current_member.show_borrow_list()
        # 直接调用用户身上的归还书籍即可,book身上自己有自增的方法
        book_id = input('请输入您想归还的书籍的图书id:').strip()

        # ——此处为 AI 补写—— 先判断书在不在系统,再取对象;否则不存在的 id 会 KeyError 崩溃
        if book_id not in self.book_dict:
            print('您想归还的书籍本系统没有哦,请输入别的书籍')
            return
        temp_book_obj = self.book_dict[book_id]
        # 判断是否存在于字典
        if temp_book_obj not in self.current_member.borrow_list:
            # 如果不存在,则提示
            # ——此处为 AI 修改—— 原文案"没有借哦没有哦"重复,已修正
            print('您想归还的书籍用户没有借哦,请输入别的书籍')
            return
        # 拿到书籍对象丢到用户归还的列表中进行对象匹配
        # 安全校验系统这边做完了,会员对象直接执行删除即可
        self.current_member.return_book(temp_book_obj)

    # 查看当前登录用户的借阅信息
    # 直接调用户身上的打印他身上自己的图书列表即可
    def show_current_borrow_list(self):
        self.current_member.show_borrow_list()

    # 查看当前系统的书籍库存信息
    def show_book_database(self):
        # 获取字典的values直接打印
        for i in self.book_dict.values():
            print(i)

    # 登录方法定义成私有,只允许在内部通过别的函数连环调用
    def __login(self):
        while True:
            # 判断当前是否有用户登录
            if self.current_member is None:
                # 当前没有用户登录,让用户输入账号进行登录操作
                # 登录方法,用户进来必须先进行登录操作
                user_id = input('请输入会员id:').strip()
                # 拿id对会员字典进行查询是否存在
                if user_id in self.member_dict:
                    # 获取会员对象
                    temp_user_obj = self.member_dict[user_id]
                    # 存在则要求输入密码
                    password = input('请输入会员密码:').strip()
                    # 验证密码是否正确
                    if temp_user_obj.password_is_true(password):
                        # 正确,登陆成功
                        self.current_member = temp_user_obj
                        # 返回true代表登陆成功
                        return True
                    else:
                        print('密码错误,请重新登录')
                        continue
                else:
                    print('当前登录的账号尚未注册,请重新登录')
                    continue

    # 定义run方法,进行系统启动
    def run_system(self):
        print('欢迎使用书籍数据库管理系统,请先登录')
        # 调用登录方法,由run方法调用,外界不允许直接调用
        if self.__login():
            # 登陆成功后,循环打印菜单,启动系统
            while True:
                print("-" * 50)
                print("-     1. 借阅图书  2. 归还图书  3. 查看当前用户借阅  4.查看库存  5. 退出系统     -")
                print("-" * 50)
                # 收集用户输入
                choice = input(f'尊敬的{self.current_member.name},请输入您想进行的操作')
                # 用户输入可能会出现bug,在这里写异常捕获保证代码健壮性
                try:
                    match choice:
                        case '1':
                            self.handle_borrow_book()
                        case '2':
                            self.handle_return_book()
                        case '3':
                            self.show_current_borrow_list()
                        case '4':
                            self.show_book_database()
                        case "5":
                            print('欢迎下次使用')
                            return
                        case _:
                            print('输入非法,请重新输入')
                except Exception as e:
                    print(f'程序异常,异常原因是:{e}')
                    print('放在用户输入这里是因为,如果出现异常,不让异常代码打断while循环的执行')


if __name__ == "__main__":
    # 实例化图书管理系统
    library_manager_system_obj = LibrarySystem()
    library_manager_system_obj.run_system()
