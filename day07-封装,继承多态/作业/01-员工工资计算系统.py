"""
员工工资计算系统
    需求说明: 某公司有三种类型的员工，基本工资相同，但奖金计算方式不同。使用抽象类规范工资计算方法。
    技术要求:
        创建抽象类 Employee
        属性：emp_id（工号）、name（姓名）、base_salary（基本工资，默认5000） ---> 参数设置默认值
        抽象方法：calculate_bonus()（计算奖金），子类必须实现
        普通方法：total_salary()（总工资 = 基本工资 + 奖金）
        普通方法：show_info()（展示员工信息）
    创建三个子类:
        Salesman（销售员）：奖金 = 销售额 × 提成比例（5%） ---> 扩充属性: 销售金额 sales_amount
        Manager（经理）：奖金固定为 3000
        Programmer（程序员）：奖金 = 完成项目数 × 500  -----> 扩充属性: 完成项目数 projects_completed
    测试程序:
        创建不同类型的员工
        计算并展示每个员工的总工资

测试代码:
# 测试代码
if __name__ == "__main__":
    employees = [
        Salesman("S001", "张三", 5000),
        Manager("M001", "李四"),
        Programmer("P001", "王五", 3)
    ]

    print("=" * 70)
    print("员工工资表")
    print("=" * 70)
    for emp in employees:
        emp.show_info()
    print("=" * 70)
"""
from abc import ABC, abstractmethod


# 定义员工类
class Employee(ABC):
    # 初始化基础属性
    def __init__(self, emp_id, name, base_salary: int | float = 5000):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    # 计算奖金的抽象方法
    @abstractmethod
    def calculate_bonus(self):
        pass

    # 计算总工资的方法
    def total_salary(self):
        return self.base_salary + self.calculate_bonus()

    # 展示员工信息的方法
    def show_info(self):
        # 计算奖金
        bonus = self.calculate_bonus()
        # 计算总工资
        total = self.total_salary()
        # 输出信息
        print(f"工号: {self.emp_id:<6} | 姓名: {self.name:<4} | 基本工资: ¥{self.base_salary:>7.2f} | "
              f"奖金: ¥{bonus:>7.2f} | 总工资: ¥{total:>8.2f}")


class Salesman(Employee):
    # 创建销售员类,并且新增一个属性
    def __init__(self, emp_id, name, sales_amount, base_salary: int | float = 5000):
        # 先调用父类的构造器绑定属性
        super().__init__(emp_id, name, base_salary)
        # 绑定销售额的属性
        self.sales_amount = sales_amount

    # 重写奖金计算方法
    def calculate_bonus(self):
        # 奖金 = 销售额 × 提成比例（5%）
        return self.sales_amount * 0.05


class Manager(Employee):
    # Manager（经理）
    # 建议显示加上构造函数,不加的话,如果没有新增,则底层自动触发父类构造器绑定属性
    def __init__(self, emp_id, name, base_salary: int | float = 5000):
        super().__init__(emp_id, name, base_salary)

    # 重写奖金计算方法
    def calculate_bonus(self):
        # 奖金固定为 3000
        return 3000


class Programmer(Employee):
    # 程序员类
    def __init__(self, emp_id, name, projects_completed, base_salary: int | float = 5000):
        super().__init__(emp_id, name, base_salary)
        # 新增属性完成项目数
        self.projects_completed = projects_completed

    # 重写奖金计算方法
    def calculate_bonus(self):
        # 奖金 = 完成项目数 × 500
        return self.projects_completed * 500


# 测试
if __name__ == "__main__":
    employees_list = [
        # 通过三个子类创建各自的对象
        Salesman("S001", "张三", 5000),
        Manager("M001", "李四"),
        Programmer("P001", "王五", 3)
    ]

    print("=" * 70)
    print("员工工资表")
    print("=" * 70)
    for emp in employees_list:
        # 循环遍历打印三个员工的信息
        emp.show_info()
    print("=" * 70)
