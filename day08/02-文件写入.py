# 写入文件的操作,通过open的内置方法
file_obj = open(file='./resources/你好小黄.txt', mode='w', encoding="utf-8")

# 对文件对象进行操作
file_obj.write('\t我是帅气的黄一个\n')
file_obj.write('和帅气的汪宸宇联盟\n')

# 写入完毕后关闭文件
file_obj.close()
