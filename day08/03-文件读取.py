# 获取文件对象
# file = open('./resources/你好小黄.txt', mode='r', encoding='utf-8')
#
# result = file.read()
# print(result)
#
# file.close()

# 读取当前面目录下的python文本文件
file = open('./01-异常捕获.py', mode='r', encoding='utf-8')
# 对文件进行操作
try:
    result = file.read()
    print(result)
finally:
    file.close()
