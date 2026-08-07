# ============================================================================
# 练习2：成绩统计分析器
# ============================================================================
#
# 题目描述：
#   设计一个函数 analyze_scores，要求功能如下：
#   1. 通过 *args 接收任意数量的分数（0~100之间的数值）
#   2. 通过 **kwargs 接收配置项：
#      - round_ndigits：结果保留的小数位数（默认 1）
#      - show_detail：是否打印详细信息（默认 False）
#      - pass_line：及格线分数（默认 60）
#   3. 返回值是一个字典，包含：
#      - count：人数
#      - max_score：最高分
#      - min_score：最低分
#      - avg_score：平均分
#      - pass_rate：及格率（以百分比字符串表示，如 "75.0%"）
#   4. 如果 show_detail=True，在函数内部打印详细统计信息
#   5. 如果未传入任何分数，返回字典中各项均为 0 或 "0%"
#   6. 添加完整的类型注解
#
#   测试：
#     analyze_scores(85,92,78,89,95,88,76,90, round_ndigits=2, show_detail=True)
#       → {'count': 8, 'max_score': 95, 'min_score': 76, 'avg_score': 86.62, 'pass_rate': '100.0%'}
#     analyze_scores(45,55,38,62,70,59, pass_line=60, round_ndigits=1)
#       → {'count': 6, 'max_score': 70, 'min_score': 38, 'avg_score': 54.8, 'pass_rate': '33.3%'}
# ============================================================================

# 定义函数
def analyze_scores(*scores,**options):
    """
    此函数统计分数，根据分数的具体情况统计人数，最高最低分，平均分和及格率是多少
    :param scores: 传入分数列表
    :param options: 传入配置项，可操作：保留小数位数，是否打印详情，修改及格线分数
    :return:    返回结果对象，包含五个关键字段
    """

    # 初始化默认配置参数
    # 结果保留几位小数，没获取到用户配置默认值为1
    round_ndigits = options.get('round_ndigits', 1)
    # 是否在数据统计完毕后打印详细信息
    show_detail = options.get('show_detail', False)
    # 及格线阈值设定
    pass_line = options.get('pass_line', 60)

    # 空值判断
    if not scores:
        # 如没传值，直接定义默认dict直接return
        empty_result = {
            "count": 0,
            "max_score": 0,
            "min_score": 0,
            "avg_score": 0,
            "pass_rate": "0%"
        }
        if show_detail:
            print("未传入任何分数！")
        return empty_result



    # 统计人数
    count = len(scores)
    # 最高分
    max_score = max(scores)
    # 最低分
    min_score = min(scores)
    # 平均分
    avg_score = round(sum(scores) / count,round_ndigits)
    # 计算及格率
    # 及格人数 / 总人数，再 * 100%
    pass_rate = f"{(len([stu_score for stu_score in scores if stu_score >= pass_line]) / count) * 100}%"

    # 返回结果拼装
    result = {
        "count": count,
        "max_score": max_score,
        "min_score": min_score,
        "avg_score": avg_score,
        "pass_rate": pass_rate
    }

    # 是否提前打印
    if show_detail:
        print(
            f"总人数：{result["count"]}。"
            f"最高分：{result["max_score"]}。"
            f"最低分：{result["min_score"]}。"
            f"平均分：{result["avg_score"]}。"
            f"及格率：{result["pass_rate"]}。"
        )

    return result

# 返回结果
print(analyze_scores(85,92,78,89,95,88,76,90,55,13,show_detail=False,round_ndigits=5,pass_line=90))