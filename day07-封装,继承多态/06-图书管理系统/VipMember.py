from Member import Member


class VipMember(Member):
    # 新增一个会员等级
    def __init__(self, member_id, name, password, vip_level=1):
        # 先调用父类的构造器
        super().__init__(member_id, name, password)
        # 再新增一个等级
        self.vip_level = vip_level

    # 重写方法
    def get_max_borrow_num(self) -> int:
        # 普通会员类只能
        return 6 + self.vip_level
