# case 后面可以定义变量来接受match后面变量的值

score = float(input('请输入考试分数'))

# 通过模式匹配来进行评分
match score:
    case num if num < 0 or num > 100:
        print('分数的范围为0-100')
    case num if num >= 90:
        print('你可真厉害')
    case num if num >= 80:
        print('还行，继续努力')
    case num if num >= 70:
        print('马马虎虎吧，平均水平')
    case num if num >= 60:
        print('刚好及格，不愧是当代大学生')
    case _:
        print('废物，这都及格不了，吃干饭的吗')

# 其实正常来说比较的就是score，直接拿score比较即可，前面填一个占位符