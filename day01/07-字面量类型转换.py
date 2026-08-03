# 大家好,我是小黄,今年18岁,我的爱好是画画和旅游
name = '黄一个'
age = 18
hobby = [
    '画画',
    'travel'
]

# 拼接字符串
result = '大家好,我是' + name + '今年' + str(age) + '岁,爱好是' + hobby[0] +hobby[1]
# 这里age需要转换类型
print(result)

# 各种字面量类型转换
score = '60.5'
score_str = float(score)
print(type(score_str))

# 布尔值转换
hello = '哈喽大家好'
hello_boolean = bool(hello)
null_str = ''
null_boolean = bool(null_str)

# 打印结果
print(hello_boolean,type(hello_boolean))
print(null_boolean,type(null_boolean))
