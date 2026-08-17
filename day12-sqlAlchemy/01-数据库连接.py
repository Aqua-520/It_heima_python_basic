from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, select, or_, func, update, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 创建数据库连接引擎

mysql_engine = create_engine(url="mysql+pymysql://root:843708301@127.0.0.1:3306/it_heima",
                             echo=False,pool_size=5,max_overflow=5,pool_recycle=3600,pool_pre_ping=True)
# 定义父类,进行匹配,类模板属性就跟表的一个个字段一一对应
class SqlBase(DeclarativeBase):
    pass

# 定义对表格字段一一匹配的对象模板类,通过创建对象的方式来创建每一条数据
class AiMessage(SqlBase):
    # 定义表格名称映射
    __tablename__ = 'chatbot_message'

    # 声明属性的类型
    id:Mapped[int] = mapped_column(type_=Integer,primary_key=True,autoincrement=True,comment='主键id')
    session_id:Mapped[int] = mapped_column(type_=Integer,nullable=False,comment='会话id')
    role:Mapped[str] = mapped_column(type_=String(20),nullable=False,comment='消息角色分类')
    content:Mapped[str] = mapped_column(type_=String(500),nullable=False,comment='消息角色分类')
    create_time:Mapped[datetime] = mapped_column(type_=DateTime,nullable=False,default=datetime.now(),comment='会话创建时间')

    def __str__(self):
        return f'(主键:{self.id}本轮会话id:{self.session_id},角色:{self.role},内容:{self.content},会话创建时间:{self.create_time})'

if __name__ == '__main__':
    # 导入Session类,将engine对象传入,返回对话实例
    with Session(mysql_engine) as session_obj:
    #     result_tuples = session_obj.execute(
    #         # execute中写查询语句
    #         # select查询所有字段
    #         select(AiMessage)
    #     ).all() # 这个all是execute身上的,返回列表元组,查询所有字段的时候0号位为一个result的结果对象
    #
    #     # 这个对象可以遍历
    #     # print(result_tuples)
    #     for item in result_tuples:
    #         # 这个item则是被包在元组里的对象地址
    #         # 直接取出元组0号位打印则是对象的所有信息
    #         print(item[0])


        # 1. 查询id为1的数据
        result = session_obj.get(AiMessage,1) # get只能根据主键查询,传入具体的表结构类,主键值为1的数据
        # result = session_obj.execute(
        #     select(AiMessage).where(AiMessage.id == 1)
        # ).scalars().one()
        # 这里查询一条语句的情况下,直接返回的是封装好的结果对象
        # print(result)


        # 2. 查询content中包含'好'字的数据
        result2 = session_obj.execute(
            select(
                AiMessage
            ).where(AiMessage.content.like('%好%'))
        ).mappings().all()

        # for item in result2:
            # print(item['AiMessage'])

        # 3. 查询session_id为1,并且role 为'user'的消息
        # result3 = session_obj.execute(
        #     select(AiMessage).where(AiMessage.session_id == 1,AiMessage.role == 'user')
        # ).scalars().all()
        # # print(result3)
        # for item in result3:
        #     print(item)

        # 4. 查询id为8,或者role为 'user'的消息
        # result4 = session_obj.execute(
        #     select(AiMessage).where(or_(AiMessage.id == 8, AiMessage.role == 'user'))
        # ).scalars().all()
        #
        # for item in result4:
        #     print(item)

        # 需求 : 查询 id 为8，或者role 为'user'的消息，并根据创建时间进行倒序排序，创建时间相同，再根据id升序排序
        # result5 = session_obj.execute(
        #     select(AiMessage).where(or_(AiMessage.id == 8,AiMessage.role == 'user'))
        #     .order_by(AiMessage.create_time.desc(),AiMessage.id.desc())
        # ).scalars().all()
        #
        # for item in result5:
        #     print(item)

        # 分页查询
        # page = 1
        # size = 3
        # result6 = session_obj.execute(
        #     select(AiMessage).offset((page-1)*size).limit(size)
        # ).scalars().all()
        # print(result6)
        # for item in result6:
        #     print(item)


        # 分组查询
        # result7 = session_obj.execute(
        #     select(AiMessage.role,func.count(1).label('my_count')).group_by(AiMessage.role).having(func.count(1) >=2)
        # ).all()
        # # 分了两个组
        # for result in result7:
        #     print(f'role={result[0]},count={result[1]}')

        # 更新字段
        # result8 = session_obj.execute(
        #     update(AiMessage).where(AiMessage.id == 8).values(
        #         # values只能传入一种参数,所有匹配的数据都会被修改
        #         content='我是被修改的role内容',create_time = datetime.now()
        #     )
        # )
        # print(result8.rowcount)

        # 通过查询拿到对象的形式进行更新
        # query_obj = session_obj.get(AiMessage,1)
        # query_obj.content = '我被修改了'
        # query_obj.create_time = datetime.now()

        # 删除
        # session_obj.execute(
        #     delete(AiMessage).where(AiMessage.id == 1)
        # )

        # 批量删除
        session_obj.execute(
            delete(AiMessage).where(AiMessage.id.in_([2,3,4,5]))
        )

        # 提交事务
        session_obj.commit()