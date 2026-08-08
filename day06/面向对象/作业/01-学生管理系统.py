# 通过面向对象的方式实现学生管理系统
# 定义学生类,每个学生对象身上有四个属性,分别是name,和两个分数

class Student:
    def __init__(self, name, math, english):
        self.name = name
        self.math = math
        self.english = english

    # 当此类的实例被直接打印的时候
    def __str__(self):
        info = f'当前学生姓名:{self.name},数学分数:{self.math},英语分数:{self.english}'
        return info


# 创建学生管理系统类
# 1.添加  2.修改  3.删除  4.查询指定学生  5.查询所有学生信息  6.退出系统 #")
class StuManager:
    # 每个学生管理系统对象身上都有一个各自独立维护的学生信息列表
    def __init__(self):
        # 直接初始化为一个空数组
        self.stu_list = []

    # 判断学生是否存已经存在于系统
    def has_student(self, name):
        for stu_item in self.stu_list:
            if stu_item.name == name:
                return stu_item
        # 循环结束没找到直接返回空
        return None

    # 判断输入的分数是否合规
    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    # 新增学生
    def add(self):
        # 收集学生姓名
        name = input('请输入需要新增的学生姓名:').strip()

        # 调用函数是否能拿到结果
        if self.has_student(name) is not None:
            print('该学生已经存在于系统,请重新输入')
            return
        # 是空则代表不存在该学生,执行后续输入
        math = float(input('请输入该学生数学成绩:'))
        # 判断两个分数是否合规
        # 通过类名来调用静态方法
        if not StuManager.is_valid_score(math):
            print('数学分数非法,请重新输入:')
            return

        english = float(input('请输入该学生英语成绩:'))
        if not StuManager.is_valid_score(english):
            print('英语分数非法,请重新输入:')
            return

            # 通过if,则创造学生对象,进行数据的保存
        student = Student(name, math=math, english=english)
        # 将学生直接丢进list保存
        self.stu_list.append(student)
        print('学生信息新增成功')

    # 修改
    def update(self):
        # 修改哪一位学生
        name = input('请输入需要修改的学生姓名:').strip()

        # 判断学生是否存在于系统,如果找不到则直接结束
        student = self.has_student(name)
        if student is None:
            print('该学生不存在,不能修改学生信息,请通过新增操作')
            return

        # 收集分数
        math = float(input('请输入该学生数学成绩:'))
        # 判断两个分数是否合规
        # 通过类名来调用静态方法
        if not StuManager.is_valid_score(math):
            print('数学分数非法,请重新输入:')
            return

        english = float(input('请输入该学生英语成绩:'))
        if not StuManager.is_valid_score(english):
            print('英语分数非法,请重新输入:')
            return

        # 修改当前的学生对象的分数属性
        student.math = math
        student.english = english
        print('学生信息修改成功')

    # 删除指定学生
    def remove_student(self):
        # 删除哪一位学生
        name = input('请输入需要删除的学生姓名:').strip()

        # 查询是否存在于系统
        student = self.has_student(name)
        if student is None:
            print('该学生不存在,请重新输入需要删除的学生姓名')
            return

        # 删除指定学生
        self.stu_list.remove(student)
        print('学生删除成功')

    # 查询指定学生信息
    def get_student_info(self):
        name = input('请输入需要查询的学生名称:').strip()

        # 判断学生是否存在于系统,如果找不到则直接结束
        student = self.has_student(name)
        if student is None:
            print('该学生不存在,查询不了具体详情')
            return

        # 存在则直接打印
        print(student)

    # 打印所有学生信息
    def get_all_student_info(self):
        # 如果没有学生信息,则打印提示
        if len(self.stu_list) == 0:
            print('当前数据库中还不存在任何学生信息,请新增')
            return

        # 循环打印
        for index, stu_info in enumerate(self.stu_list):
            print(f"{index + 1}号学生信息:{stu_info}")

    # 系统启用的方法
    def start_manager_system(self):
        print('正在启动学生信息管理系统')
        while True:
            # 打印菜单
            print("-" * 50)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生   2.修改学生   3.删除学生  4.查询指定学生   5.查询所有学生  6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("-" * 50)
            # 用户操作
            user_input = input('请选择您需要进行的操作:').strip()

            match user_input:
                case '1':
                    # 新增
                    self.add()
                case '2':
                    # 修改
                    self.update()
                case '3':
                    self.remove_student()
                case '4':
                    self.get_student_info()
                case '5':
                    self.get_all_student_info()
                case '6':
                    print('退出系统')
                    return
                case _:
                    print('输入非法,请重新根据菜单进行输入')
                    continue


if __name__ == '__main__':
    # 开发环境,获取管理系统实例
    stu_manager_system_obj = StuManager()
    # 启动
    stu_manager_system_obj.start_manager_system()
