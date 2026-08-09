# 导入基类进行继承
from Member import Member


# 定义普通会员类
class NormalMember(Member):
    # 继承后重写可借取最大书籍的方法

    def get_max_borrow_num(self) -> int:
        # 普通会员类只能
        return 3
