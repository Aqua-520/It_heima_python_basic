# 字典的key可以为任意不可变类型
dict1 = {
    520:'我是一哥',
    13.14:True,
    False:'也可以用布尔值作为key',
    ('name',111):"元组也可以拿来作为key",
    520:'key重名，后面的覆盖前面的'
}
print(dict1)

# value可以为任何类型
user = {
    "name":"黄一个",
    "age":18,
    "hobby":['画画','travel'],
    "score":{
        "math":250,
        "c#":150
    }
}
print(user['score']['math'])

# 修改画画爱好为打王者
user['hobby'][0] = '打王者荣耀'
print(user['hobby'][0])