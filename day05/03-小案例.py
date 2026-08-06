# 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）
# 函数名称  count_vowel (遵循标识符命名规范)
# 函数参数  字符串
# 函数返回  个数
def count_vowel(string):  # hello world
    """
    此函数接收一个字符串，返回统计元音字母的个数
    :param string: 输入的英文字符串
    :return : total 元音字母个数
    """
    total = 0
    for char in string:
        if char in 'aeiouAEIOU':
            total += 1

    # 返回统计结果
    return total

print(f'元音字母输入的结果是{count_vowel("caonimade")}')


# 2．定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回
# 函数名称 : calc_max_min_avg
# 函数参数 : 班级学员高考成绩列表 [560,720,600,520,200,425]
# 函数返回 : 最高分、最低分、平均分
def calc_max_min_avg(list):
    """
    传入分数列表，进行最高分，最低分统计，包括
    :param list: 传入list可迭代列表
    :return: 返回统计好的dict对象
    """
    return {
        "最高分":max(list),
        "最低分":min(list),
        "平均分":round(sum(list) / len(list),5)
    }
print(calc_max_min_avg([1,2,3,4,5]))