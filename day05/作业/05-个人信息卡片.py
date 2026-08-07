
# ============================================================================
# 练习3：个人信息卡片
# 知识点：默认参数 + 关键字参数 + **kwargs + 类型注解
# ============================================================================
#
# 题目描述：
#   设计一个函数 create_profile，用于生成个人信息卡片。要求如下：
#   1. 函数接收以下参数（均有默认值）：
#      - name：姓名（默认 "未填写"）
#      - age：年龄（默认 0）
#      - city：城市（默认 "未知"）
#      - job：职业（默认 "待业"）
#      - hobby：爱好（默认 "无"）
#   2. 除了上述参数外，还可以通过 **kwargs 接收任意自定义信息
#      （如 phone="138xxxx", email="abc@test.com"）
#   3. 函数返回一个格式化好的多行字符串（个人信息卡片），形如：
#      ===== 个人信息卡 =====
#      姓名: 张三
#      年龄: 25
#      城市: 北京
#      职业: 程序员
#      爱好: 篮球
#      --- 其他信息 ---
#      手机: 138xxxx
#      邮箱: abc@test.com
#      ======================
#   4. 添加完整的类型注解
#
#   测试：
#     create_profile("张三", 25, "北京", "程序员", "篮球",
#                    phone="138xxxx", email="abc@test.com")
#     create_profile("李四", city="上海", hobby="摄影")
#     create_profile()
# ============================================================================

def create_profile(name:str ='未填写',age:int =0,city:str ='未知',job:str ='待业',hobby:str ='无',**others_info) -> str:
    result_str = f"""
===== 个人信息卡 =====
姓名: {name}
年龄: {age}
城市: {city}
职业: {job}
爱好: {hobby}
"""

    # 检测是否传入了其他信息
    if others_info:
        other_str = ''
        # 如有信息，进行字符串拼接
        lines = [f"{key}: {value}"for key,value in others_info.items()]
        # 每一条的字符串和下一条字符串之间增加\n换行符，join函数的作用
        other_str = "----- 其他信息 -----\n" + "\n".join(lines) + "\n"
        result_str += other_str
        result_str += "===================="

    return result_str

# 其他信息字典
info = {
    "phone":"123123",
    "contry":'Japan'
}
print(create_profile(**info))