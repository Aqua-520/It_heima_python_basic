# 随机生成一个字典
import random

names = ["王林", "韩立", "紫灵", "厉飞雨", "天运子", "遁天", "曾牛"]

user_dict = {}

for name in names:
    # 通过随机数进行生成
    user_dict[name] = random.randint(60, 100)

print(f'初始字典：{user_dict}')

print('-' * 50)

# 根据key查询值，或者get方法
# value1 = user_dict['王林']
value1 = user_dict.get('王林')
print(value1)

# 如果get函数找不到，则可以在第二个参数的位置设置默认值
value2 = user_dict.get('黄一个','黄一个无敌')
print(value2)

print('-' * 50)
# 删除元素，通过del关键字或者是pop传入key
del user_dict['遁天']
# pop会返回value
result = user_dict.pop('曾牛')
print(f"删除后的结果是{user_dict}")

print('-' * 50)

# 遍历字典，此方法会返回list，把key或者value放入list中返回，然后通过遍历拿到需要的东西
keys = user_dict.keys()
values = user_dict.values()

for i in user_dict:
    # 直接遍历dict，拿到的是key
    print(user_dict[i])

print('-' * 50)
# items方法返回元组
user_tuples = user_dict.items()
for key,value in user_tuples:
    print(f'key是：{key}，value是{value}')