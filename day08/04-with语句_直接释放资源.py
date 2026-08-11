# with是一个资源管理器
# 上下文管理器的语法糖
# 用于确保代码块执行完毕后，无论是否发生异常，都能自动且安全地释放资源

with open(file='./03-文件读取.py', mode='r', encoding='utf-8') as f:
    # 读取文件对象
    result = f.read()
    print(result)
    # 不需要close,文件资源会被自动释放
