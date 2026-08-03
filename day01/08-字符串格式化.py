"""
    通过三种字符串格式化的方式,快速实现变量的填充
    因为老是不断地拼接非常的麻烦
"""

# 连锁打印
name = '黄一个'
age = 18
hobby = [
    '画画',
    'travel'
]
# 通过占位符的方式
print('大家好我叫:%s,今年%s,爱好是:%s,%s'% (name,age,hobby[0],hobby[1]))
# 使用format,字符串原型链对象自带的方法
print('大家好我叫:{},今年{},爱好是:{},{}'.format(name,age,hobby[0],hobby[1]))
# 使用format模版字符串简写
print(f'大家好我叫:{name},今年{age},爱好是:{hobby[0]},{hobby[1]}')