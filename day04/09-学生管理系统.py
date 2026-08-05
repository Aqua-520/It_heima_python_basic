"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用教务管理系统")

student_scores = {
    # 加一个默认值，免得调起来麻烦
    "黄一个":{
        "chinese":100.0,
        "english":100.0,
        "math":100.0
    },
    "李明": {
        "chinese": 88.0,
        "english": 76.5,
        "math": 92.0
    },
    "王小雨": {
        "chinese": 92.0,
        "english": 88.0,
        "math": 76.5
    },
    "张浩然": {
        "chinese": 75.0,
        "english": 82.0,
        "math": 88.0
    },
    "刘西西": {
        "chinese": 100.0,
        "english": 66.0,
        "math": 55.5
    },
}

# 判断某个key是否存在于dict之中的函数，存在返回True，不存在返回False
def is_in_student_system(key):
    return key in student_scores

while True:
    # 打印欢迎界面
    print(menu)

    # 判断用户输入的菜单信息
    user_control = input('请输入操作符：').strip()

    match user_control:
        case '1':
            # 1. 添加学生信息
            name = input('请输入需要新增的学生姓名：').strip()

            if is_in_student_system(name):
                # 如果存在了，会冲突，直接跳过
                print('您需要新增的学生信息已经存在')
                continue
            # 执行新增操作
            chinese = float(input('请输入语文成绩：'))
            math = float(input('请输入数学成绩：'))
            english = float(input('请输入英语成绩：'))

            # 封装进对象中
            student_scores[name] = {
                "chinese":chinese,
                "math":math,
                "english":english
            }

        case '2':
            # 2. 修改学生信息
            name = input('请输入需要修改的学生姓名：').strip()

            if not is_in_student_system(name):
                # 如果不存在，你修改个毛
                print('您想修改的学生信息不存在')
                continue

            # 二级菜单：单独修改某一科成绩
            print('请选择需要修改的科目：')
            print('1. 语文    2. 数学    3. 英语')
            subject = input('请输入操作符：').strip()

            match subject:
                case '1':
                    # 修改语文
                    student_scores[name]["chinese"] = float(input('请输入语文成绩：'))
                    print('修改成功')
                case '2':
                    # 修改数学
                    student_scores[name]["math"] = float(input('请输入数学成绩：'))
                    print('修改成功')
                case '3':
                    # 修改英语
                    student_scores[name]["english"] = float(input('请输入英语成绩：'))
                    print('修改成功')
                case _:
                    print('输入非法，请重试')

        case '3':
            # 3. 删除学生信息
            name = input('请输入需要删除的学生姓名：').strip()

            if not is_in_student_system(name):
                # 如果不存在，你删个勾八啊
                print('您想删除的学生信息不存在')
                continue

            del student_scores[name]
            print('删除成功')

        case '4':
            # 4. 根据姓名查询单条学生信息
            name = input('请输入需要查询的学生姓名：').strip()

            if not is_in_student_system(name):
                # 如果不存在，你删个勾八啊
                print('您想查询的学生信息不存在')
                continue

            # 打印单条学生信息
            print(f'学生：{name}，语文成绩：{student_scores[name]["chinese"]}，数学成绩：{student_scores[name]["math"]}，'
                  f'英语成绩：{student_scores[name]["english"]}')
        case '5':
            # 5. 列出所有学生，制表
            print('姓名 \t 语文 \t 数学 \t 英语')
            for name,scores in student_scores.items():
                # 遍历对象
                print(f'{name} \t {scores["chinese"]} \t {scores["math"]} \t {scores["english"]}')
        case '6':
            # 6. 统计班级成绩
            # 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。

            result = {
                "chinese":{
                    "min":0,
                    "max":0,
                    "avg":0.0,
                    "max_stu":[],
                    "min_stu":[]
                },
                "math":{
                    "min": 0,
                    "max": 0,
                    "avg": 0.0,
                    "max_stu": [],
                    "min_stu": []
                },
                "english":{
                    "min": 0,
                    "max": 0,
                    "avg": 0.0,
                    "max_stu": [],
                    "min_stu": []
                }
            }
            # 计算最高最低分和平均分
            all_chinese = []
            all_math = []
            all_english = []
            for name,scores in student_scores.items():
                # 拿到每一个分，分批存入数组
                all_chinese.append(scores['chinese'])
                all_math.append(scores['math'])
                all_english.append(scores['english'])
                # 存储完毕，计算大小值
                result['chinese']['min'] = min(all_chinese)
                result['chinese']['max'] = max(all_chinese)
                result['chinese']['avg'] = sum(all_chinese) / len(student_scores)

                result['math']['min'] = min(all_math)
                result['math']['max'] = max(all_math)
                result['math']['avg'] = sum(all_math) / len(student_scores)

                result['english']['min'] = min(all_english)
                result['english']['max'] = max(all_english)
                result['english']['avg'] = sum(all_english) / len(student_scores)

            # 第二条循环，将最高分和最低分的学生姓名丢进去
            result['chinese']['max_stu'] = [name for name,scores in student_scores.items() if
                                            result['chinese']['max'] == student_scores[name]["chinese"]]
            result['chinese']['min_stu'] = [name for name,scores in student_scores.items() if
                                            result['chinese']['min'] == student_scores[name]["chinese"]]

            result['math']['max_stu'] = [name for name, scores in student_scores.items() if
                                            result['math']['max'] == student_scores[name]["math"]]
            result['math']['min_stu'] = [name for name, scores in student_scores.items() if
                                            result['math']['min'] == student_scores[name]["math"]]

            result['english']['max_stu'] = [name for name, scores in student_scores.items() if
                                         result['english']['max'] == student_scores[name]["english"]]
            result['english']['min_stu'] = [name for name, scores in student_scores.items() if
                                         result['english']['min'] == student_scores[name]["english"]]

            # 输出统计结果
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {result['chinese']['max']}, 最低分: {result['chinese']['min']}, 平均分: {result['chinese']['avg']:.2f}")
            print(f"     最高分学生: {result['chinese']['max_stu']}")
            print(f"     最低分学生: {result['chinese']['min_stu']}")

            print(
                f"数学 - 最高分: {result['math']['max']}, 最低分: {result['math']['min']}, 平均分: {result['math']['avg']:.2f}")
            print(f"     最高分学生: {result['math']['max_stu']}")
            print(f"     最低分学生: {result['math']['min_stu']}")

            print(
                f"英语 - 最高分: {result['english']['max']}, 最低分: {result['english']['min']}, 平均分: {result['english']['avg']:.2f}")
            print(f"     最高分学生: {result['english']['max_stu']}")
            print(f"     最低分学生: {result['english']['min_stu']}")
            print("========================")
        case '7':
            print('退出了，拜拜')
            break
        case _:
            print('输入非法，请重试')
