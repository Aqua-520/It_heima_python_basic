# 1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
#   1. 分数 >= 90：A
#   2. 分数 >= 75：B
#   3. 分数 >= 60：C
#   4. 分数 < 60：D
def score_to_grade(score: int|float) -> str:
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "c"
    else:
        return "D"
# print(score_to_grade(100))


#   2. 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
#   把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# print(is_palindrome("黄山落叶松叶落山黄"))

# 3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def onvert_seconds(total_seconds):
    # 时 整除3600,看看能得到几轮,剩下不足的秒数不要了
    hour = total_seconds // 3600
    # 分 将时拿去后的剩余秒数 对60做整除
    minutes = (total_seconds % 3600) // 601
    # 秒,拿对60的余数,就是当前60以内的剩余秒
    seconds = total_seconds % 60
    # 将数值转化为字符串,然后通过内置zfill方法进行补0,最少为两位
    return f"当前转换后的时间为:{str(hour).zfill(2)}时,{str(minutes).zfill(2)}分,{str(seconds).zfill(2)}秒"

# print(onvert_seconds(50000))

# 4. 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def classify_triangle(a,b,c):
    # 通过剩余参数直接接收三条边
    # 先判断是否能构成三角形
    if not ((a + b) > c and (a + c) > b and (c + b) > a):
        # 不满足任意两边大于第三边,不是三角形
        print('不满足任意两边大于第三边,不是三角形')
        return False
    elif a == b and a == c and b == c:
        # 三边相等,为等边三角形
        print("三边相等,为等边三角形")
        return True
    elif a == b or a == c or b == c:
        # 满足两边相等的情况,为等腰三角形
        print("满足两边相等的情况,为等腰三角形")
        return True
    else:
        print("普通三角形")
        return True

classify_triangle(10,11,12)