from sqlalchemy import create_engine, Integer, String, DateTime, Date, delete, update, select, and_
from sqlalchemy.dialects.mysql import TINYINT,DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import date,datetime

# 创建数据库连接引擎
homework_engine = create_engine(
    url='mysql+pymysql://root:843708301@localhost:3306/homework',
    echo=False,
    max_overflow=2,
    pool_size=1,
    pool_recycle=7200,
    pool_pre_ping=True
)

# 引入基类
class Base(DeclarativeBase):
    pass

# 创建表结构数据模板,实例对象为一条一条数据
class HomeWorkEmp(Base):
    # 定义表格名称映射
    __tablename__ = 'homework_employee'

    id: Mapped[int] = mapped_column(type_=Integer,primary_key=True,autoincrement=True,comment='主键')
    name:Mapped[str] = mapped_column(type_=String(10),nullable=True,comment='姓名')
    gender:Mapped[int] = mapped_column(type_=TINYINT(unsigned=True),nullable=True,default=0,comment='男0,女1')
    job:Mapped[int] = mapped_column(type_=TINYINT(unsigned=True),nullable=True,comment='1:班主任, 2:讲师, 3:学工主管, 4:教研主管, 5:咨询师')
    salary:Mapped[float|int] = mapped_column(type_=DECIMAL(precision=10, scale=2, unsigned=True),nullable=True,comment='工资')
    entry_date:Mapped[date] = mapped_column(type_=Date,nullable=False,default=datetime.today(),comment='加入公司时间')
    create_time:Mapped[datetime] = mapped_column(type_=DateTime,nullable=False,default=datetime.now(),comment='数据创建时间')
    update_time:Mapped[datetime] = mapped_column(type_=DateTime,nullable=False,default=datetime.now(),comment='数据修改时间')

    def __str__(self):
        return f'(主键:{self.id},姓名:{self.name},性别:{self.gender},工作:{self.job},工资:{self.salary})'

data_list = [
    HomeWorkEmp(name='张伟', gender=0, job=1, salary=5000.00, entry_date=datetime(2020,1,1), create_time=datetime(2020,1,2), update_time=datetime(2020,1,3)),
    HomeWorkEmp(name='王芳', gender=1, job=2, salary=5500.00, entry_date=datetime(2020,1,2), create_time=datetime(2020,1,3), update_time=datetime(2020,1,4)),
    HomeWorkEmp(name='李娜', gender=0, job=3, salary=6000.00, entry_date=datetime(2020,1,3), create_time=datetime(2020,1,4), update_time=datetime(2020,1,5)),
    HomeWorkEmp(name='赵磊', gender=1, job=4, salary=6500.00, entry_date=datetime(2020,1,4), create_time=datetime(2020,1,5), update_time=datetime(2020,1,6)),
    HomeWorkEmp(name='陈静', gender=0, job=5, salary=7000.00, entry_date=datetime(2020,1,5), create_time=datetime(2020,1,6), update_time=datetime(2020,1,7)),
    HomeWorkEmp(name='周涛', gender=1, job=1, salary=7500.00, entry_date=datetime(2020,1,6), create_time=datetime(2020,1,7), update_time=datetime(2020,1,8)),
    HomeWorkEmp(name='吴洋', gender=0, job=2, salary=8000.00, entry_date=datetime(2020,1,7), create_time=datetime(2020,1,8), update_time=datetime(2020,1,9)),
    HomeWorkEmp(name='孙悦', gender=1, job=3, salary=8500.00, entry_date=datetime(2020,1,8), create_time=datetime(2020,1,9), update_time=datetime(2020,1,10)),
    HomeWorkEmp(name='马丁', gender=0, job=4, salary=9000.00, entry_date=datetime(2020,1,9), create_time=datetime(2020,1,10), update_time=datetime(2020,1,11)),
    HomeWorkEmp(name='朱婷', gender=1, job=5, salary=9500.00, entry_date=datetime(2020,1,10), create_time=datetime(2020,1,11), update_time=datetime(2020,1,12)),
    HomeWorkEmp(name='胡军', gender=0, job=1, salary=10000.00, entry_date=datetime(2020,1,11), create_time=datetime(2020,1,12), update_time=datetime(2020,1,13)),
    HomeWorkEmp(name='郭敏', gender=1, job=2, salary=10500.00, entry_date=datetime(2020,1,12), create_time=datetime(2020,1,13), update_time=datetime(2020,1,14)),
    HomeWorkEmp(name='林峰', gender=0, job=3, salary=11000.00, entry_date=datetime(2020,1,13), create_time=datetime(2020,1,14), update_time=datetime(2020,1,15)),
    HomeWorkEmp(name='何晴', gender=1, job=4, salary=11500.00, entry_date=datetime(2020,1,14), create_time=datetime(2020,1,15), update_time=datetime(2020,1,16)),
    HomeWorkEmp(name='高峰', gender=0, job=5, salary=12000.00, entry_date=datetime(2020,1,15), create_time=datetime(2020,1,16), update_time=datetime(2020,1,17)),
    HomeWorkEmp(name='罗辉', gender=1, job=1, salary=12500.00, entry_date=datetime(2020,1,16), create_time=datetime(2020,1,17), update_time=datetime(2020,1,18)),
    HomeWorkEmp(name='郑爽', gender=0, job=2, salary=13000.00, entry_date=datetime(2020,1,17), create_time=datetime(2020,1,18), update_time=datetime(2020,1,19)),
    HomeWorkEmp(name='梁宇', gender=1, job=3, salary=13500.00, entry_date=datetime(2020,1,18), create_time=datetime(2020,1,19), update_time=datetime(2020,1,20)),
    HomeWorkEmp(name='谢琳', gender=0, job=4, salary=14000.00, entry_date=datetime(2020,1,19), create_time=datetime(2020,1,20), update_time=datetime(2020,1,21)),
    HomeWorkEmp(name='韩雪', gender=1, job=5, salary=14500.00, entry_date=datetime(2020,1,20), create_time=datetime(2020,1,21), update_time=datetime(2020,1,22))
]

# 创建会话对象
with Session(homework_engine) as  session:
# 批量新增
#     session.add_all(data_list)

# -- 1. 插入数据, 员工信息：张明明，男，薪资12000，职位讲师
#     session.add(
#         HomeWorkEmp(name='张明明',gender=0,salary=12000,job=2)
#     )
# -- 2. 新增员工记录：王丽丽，女，薪资9800，职位班主任
#     session.add(
#         HomeWorkEmp(
#             name='王李莉莉',
#             gender=1,
#             salary=9800,
#             job= 1
#         )
#     )
# -- 3. 批量插入两条新员工记录（自拟合理数据）
#     list = [
#         HomeWorkEmp(name='岸本齐史',gender=1,salary=3980,job=3),
#         HomeWorkEmp(name='尾田荣一郎',gender=1,salary=22789,job=5)
#     ]
#     session.add_all(list)
# -- 4. 删除薪资低于4600的员工记录
#     result = session.execute(
#         delete(HomeWorkEmp).where(HomeWorkEmp.salary < 4600)
#     )
#     print(result.rowcount)
# -- 5. 将职位为NULL的员工的职位统一设置为班主任（job=1）
#     result = session.execute(
#         update(HomeWorkEmp).where(HomeWorkEmp.job == None).values(job = 1)
#     )
#     print(result.rowcount)
# -- 6. 修改id=7员工的职位为讲师（job=2）
#     emp = session.get(HomeWorkEmp,7)
#     emp.job = 2

# -- 7. 查询所有女性员工（gender=2）的姓名和职位
#     result = session.execute(
#         select(HomeWorkEmp.name,HomeWorkEmp.job).where(HomeWorkEmp.gender == 1)
#     ).mappings().all()
#     print(result)
#     for item in result:
#         print(item)
# -- 8. 显示薪资超过15000的员工姓名、职位和薪资
#     result = session.execute(
#         select(HomeWorkEmp.name,HomeWorkEmp.salary,HomeWorkEmp.job).where(HomeWorkEmp.salary > 15000)
#     ).mappings().all()
#     print(result)
# -- 9. 查询所有班主任（job=1）的信息，按入职日期倒序排列
#     result = session.execute(
#         select(HomeWorkEmp).where(HomeWorkEmp.job == 1).order_by(HomeWorkEmp.entry_date.desc())
#     ).scalars().all()
#
#     for item in result:
#         print(item)
# -- 10. 列出薪资在5000-8000之间的咨询师（job=5）姓名 和 薪资, 并且按照薪资倒序排序
#     result = session.execute(
        # 或者通过between函数
        # select(HomeWorkEmp.name,HomeWorkEmp.salary).where(HomeWorkEmp.job == 5,HomeWorkEmp.salary <= 8000,HomeWorkEmp.salary >= 5000)
        # .order_by(HomeWorkEmp.salary.desc())
    #     select(HomeWorkEmp.name,HomeWorkEmp.salary).where(
    #         HomeWorkEmp.job == 5,
    #         HomeWorkEmp.salary.between(5000,8000)
    #     )
    # ).mappings().all()
    # print(result)
# -- 11. 显示所有员工的姓名和薪资，按薪资从高到低排序, 如果薪资相同再按入门日期升序排序
#     result = session.execute(
#         select(HomeWorkEmp.name,HomeWorkEmp.salary).order_by(HomeWorkEmp.salary.desc(),HomeWorkEmp.entry_date.asc())
#     ).mappings().all()
#     print(result)
# -- 12. 找出薪资排名前三的员工姓名和薪资
#     result = session.execute(
#         select(HomeWorkEmp.name,HomeWorkEmp.salary).order_by(HomeWorkEmp.salary.desc()).offset(0).limit(3)
#     ).mappings().all()
#     print(result)
# -- 13. 查询2010-01-01年之后入职 并且 性别为女 并且 姓名为两个字的 员工姓名, 薪资, 职位
#     result = session.execute(
#         select(HomeWorkEmp.name,HomeWorkEmp.salary,HomeWorkEmp.job).where(HomeWorkEmp.entry_date > '2010-01-01',HomeWorkEmp.gender == 1,HomeWorkEmp.name.like('__'))
#     ).mappings().all()
#     for i in result:
#         print(i)
# -- 14. 查询所有姓"李"的员工记录
#     result = session.execute(
#         select(HomeWorkEmp).where(HomeWorkEmp.name.like('李%'))
#     ).scalars().all()
#     print(result[0])
# -- 15. 查询薪资高于20000的男性员工信息
    result = session.execute(
        select(HomeWorkEmp).where(and_(HomeWorkEmp.salary >= 20000,HomeWorkEmp.gender == 0))
    ).scalars().all()
    print(result[0])




    session.commit()