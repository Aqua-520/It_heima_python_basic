# ================================================================================
# 作业题 2：电影信息管理系统
# ================================================================================
"""
【需求说明】

1. 业务背景
   使用面向对象思想，开发一个电影信息管理系统，可对电影信息进行
   添加、修改、删除、精确查询、查询所有、查询评分最高等操作。

3. 业务规则
   3.1 添加电影时：
       - 依次输入电影名、导演、主演、票价、评分
       - 电影名不能重复（已存在则提示并返回）
       - 票价必须大于 0，评分必须在 0-10 之间，否则提示并返回
   3.2 修改电影时：
       - 输入要修改的电影名
       - 若不存在则提示"未找到该电影"
       - 找到后依次输入新的导演、主演、票价、评分，并更新
   3.3 删除电影时：
       - 输入要删除的电影名
       - 若不存在则提示"未找到该电影"
   3.4 查询电影时：
       - 输入电影名进行精确查询
   3.5 查询评分最高电影时：
       - 遍历 movie_list 找到评分最高的电影
       - 若有并列最高分，则一并输出

4. 菜单
       1. 添加电影   2. 修改电影   3. 删除电影
       4. 查询指定电影  5. 查询所有电影
       6. 查询评分最高电影  7. 退出系统
"""


# 2.1
# Movie（电影类）
# - 实例属性：电影名(name)、导演(director)、主演(actor)、票价(price)、评分(score)
# - 方法：
# *__init__：初始化方法
# *__str__：返回电影的字符串表示，格式为：
# "电影名: xxx | 导演: xxx | 主演: xxx | 票价: xxx | 评分: xxx"
# *update_info：支持更新电影信息

class Movie:
    def __init__(self, name, director, actor, price, score):
        # 实例绑定五个属性
        self.name = name
        self.director = director
        self.actor = actor
        self.price = price
        self.score = score

    # 电影信息输出
    def __str__(self):
        return f"电影名: {self.name} | 导演: {self.director} | 主演: {self.actor} | 票价: {self.price} | 评分: {self.score}"

    # 更新电影信息的方法
    def update_info(self, director, actor, price, score):
        # 更新电影信息的方法
        self.director = director
        self.actor = actor
        self.price = price
        self.score = score


# 2.2 MovieSystem（电影信息管理系统类）
#        - 类属性：system_name（系统名称）、system_version（系统版本号）
#        - 实例属性：movie_list（用于存放所有电影对象的列表）
#        - 方法：
#            * __init__：初始化方法，创建一个空的 movie_list
#            * add_movie：添加电影
#            * update_movie：修改电影
#            * delete_movie：删除电影
#            * query_movie：精确查询指定电影
#            * list_movies：展示所有电影
#            * top_rated_movie：查询评分最高的电影（若有并列，一并输出）
#            * run：显示菜单并循环接收用户操作
class MovieSystem:
    # 类的名称
    system_name = '我是电影信息管理系统'
    system_version = '1.0.0'

    # 构造函数的定义
    def __init__(self, mock=True):
        # 创造每个电影系统实例单独保存的电影信息列表
        self.movie_list = []
        # 开启初始化
        if mock:
            # 调用假数据函数
            self._init_mock_data()

    # 定义一个制造mock数据的函数
    def _init_mock_data(self):
        # 2. 定义包含多部电影对象的列表
        default_movies = [
            Movie("战狼2", "吴京", "吴京 / 弗兰克·格里罗", 60.0, 8.9),
            Movie("长津湖", "陈凯歌 / 林超贤 / 徐克", "吴京 / 易烊千玺", 65.0, 9.5),
            Movie("流浪地球2", "郭帆", "吴京 / 刘德华 / 李雪健", 70.0, 9.5),  # 与长津湖并列最高分，方便测选项6
            Movie("红海行动", "林超贤", "张译 / 黄景瑜 / 海清", 55.0, 9.2),
            Movie("建军大业", "刘伟强", "刘烨 / 朱亚文 / 黄志忠", 45.0, 8.6)
        ]
        # 推入默认列表
        # extend接收一个可迭代的容器,将内容依次推入数组
        self.movie_list.extend(default_movies)

    # 这里我们需要访问实例对象身上的list列表,如果改成静态方法则拿不到实例对象,需要从add函数中通过参数的形式传递进来
    def find_movie_name(self, name):
        for item in self.movie_list:
            if item.name == name:
                # 找到了将当前电影信息对象返回出去
                return item
        return None

    # 添加电影
    def add_movie(self):
        movie_name = input('请输入您要添加的电影名称:').strip()
        # 查询某个电影是否存在于系统
        find_result = self.find_movie_name(movie_name)
        if find_result is not None:
            # 如果不是空则代表重名了,不允许新增电影
            print('您想新增的电影,已经存在于数据库中了')
            return

        # 启用新增,收集电影信息
        director = input('请输入导演:').strip()
        actor = input('请输入主演:').strip()

        # 票价必须大于 0，评分必须在 0-10 之间，否则提示并返回
        price = float(input('票价必须大于 0,请输入票价:'))
        if price <= 0:
            print("票价必须大于0,不允许设置为0或者负数")
            return

        score = float(input('评分必须在 0-10 之间,请输入评分:'))
        if not 0 <= score <= 10:
            print("分必须在 0-10 之间")
            return

        # 通过安全校验,收集电影信息
        # 实例化电影对象
        movie_obj = Movie(movie_name, director, actor, price, score)
        # 推进系统数组中进行保存
        self.movie_list.append(movie_obj)
        print('新增电影信息成功')

    # update_movie：修改电影
    def update_movie(self):
        movie_name = input('请输入您要修改的电影名称:').strip()

        # 查询某个电影是否存在于系统
        find_result = self.find_movie_name(movie_name)
        if find_result is None:
            # 如果没有找到电影对象数据
            print('您想修改的电影不存在哦')
            return

        # 找到了直接收集用户数据进行更新操作
        director = input('请输入导演:').strip()
        actor = input('请输入主演:').strip()

        # 票价必须大于 0，评分必须在 0-10 之间，否则提示并返回
        price = float(input('票价必须大于 0,请输入票价:'))
        if price <= 0:
            print("票价必须大于0,不允许设置为0或者负数")
            return
        # 评分信息
        score = float(input('评分必须在 0-10 之间,请输入评分:'))
        if not 0 <= score <= 10:
            print("分必须在 0-10 之间")
            return

        # 调用实例对象身上的更新方法
        find_result.update_info(director, actor, price, score)
        print('更新电影信息成功')

    # 删除电影
    def delete_movie(self):
        movie_name = input('请输入您要删除的电影名称:').strip()

        # 查询某个电影是否存在于系统
        find_result = self.find_movie_name(movie_name)
        if find_result is None:
            # 如果没有找到电影对象数据
            print('您想删除的电影不存在哦')
            return

        # 找到了的话直接删除
        self.movie_list.remove(find_result)
        print('删除成功')

    # query_movie：精确查询指定电影
    def query_movie(self):
        movie_name = input('请输入您要查询的指定电影名称:').strip()

        # 查询某个电影是否存在于系统
        find_result = self.find_movie_name(movie_name)
        if find_result is None:
            # 如果没有找到电影对象数据
            print('您想查询的电影信息不存在哦')
            return

        # 查到了直接打印即可
        print(find_result)

    # list_movies：展示所有电影
    def list_movies_log(self):
        if len(self.movie_list) == 0:
            print('当前数据库中电影信息数量为空')
            return

        # 循环打印输出
        for item in self.movie_list:
            print(item)

    # top_rated_movie：查询评分最高的电影（若有并列，一并输出）
    def top_rated_movie(self):
        if len(self.movie_list) == 0:
            print('当前数据库中电影信息数量为空')
            return

        # 查询评分最高的电影
        max_movie_score = max([item.score for item in self.movie_list])

        # 根据最高分再次循环进行匹配
        # 改写成列表推导式的写法
        max_movie = [item for item in self.movie_list if item.score == max_movie_score]
        # for item in self.movie_list:
        #     if item.score == max_movie_score:
        #         # 如果当前电影对象的评分等于最高分,则将此对象推入结果数组,因为可能会有同分数,求并列
        #         max_movie.append(item)

        # 直接打印结果并return出去

        print('最高分的电影信息是')
        for item in max_movie:
            # 详细打印每一条电影对象
            print(item)

        # 返回最高分电影数组
        return max_movie

    # run：显示菜单并循环接收用户操作
    # 运行电影信息管理系统
    def run(self):
        print('电影管理系统正在启动...........')

        while True:
            # 打印菜单
            print("=" * 40)
            print(f"  {self.system_name}")
            print(f"  版本: {self.system_version}")
            print("=" * 40)
            print("  1. 添加电影")
            print("  2. 修改电影")
            print("  3. 删除电影")
            print("  4. 查询指定电影")
            print("  5. 查询所有电影")
            print("  6. 查询评分最高电影")
            print("  7. 退出系统")
            print("-" * 40)

            choice = input("  请输入您的操作编号: ").strip()
            match choice:
                case '1':
                    self.add_movie()
                case '2':
                    self.update_movie()
                case '3':
                    self.delete_movie()
                case '4':
                    self.query_movie()
                case '5':
                    self.list_movies_log()
                case '6':
                    self.top_rated_movie()
                case '7':
                    print('退出系统')
                    return
                case _:
                    print('输入非法,请重试')
                    continue


if __name__ == '__main__':
    movie_system = MovieSystem()
    movie_system.run()
