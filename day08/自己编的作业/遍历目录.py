import os

# 1. 获取当前工作目录下的所有文件和文件夹名称列表
# TODO: 使用 os.listdir() 获取文件列表
# 获取当前目录下的文件
items = os.listdir('./')

print("当前目录下的所有 Python 文件：")
for item in items:
    # 2. 判断该项是否以 ".py" 结尾，且是一个文件（非文件夹）
    # TODO: 使用 str.endswith('.py') 和 os.path.isfile()
    if item.endswith(".py") and os.path.isfile(item):
        print(f"- {item}")
