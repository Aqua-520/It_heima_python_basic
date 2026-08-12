import os

# 打印分隔符
print(os.sep)

# 1. 获取当前工作目录的绝对路径
# TODO: 使用 os.getcwd() 获取当前路径并赋值给 current_dir
# 指的当前敲下终端命令的时候在哪个目录,我可以在目录外启动这个程序
# 这也就是后期切换工作目录的核心原理
current_dir = os.getcwd()
print(current_dir)

# 2. 拼接一个名为 "test_dir" 的子目录路径（注意：不要用字符串直接相加，要用跨平台安全的函数）
# TODO: 使用 os.path.join 拼接 current_dir 和 "test_dir"
target_path = os.path.join(current_dir, 'test_dir')
print(target_path)

# 3. 检查这个路径是否已经存在，如果不存在则创建该目录
# TODO: 使用 os.path.exists() 检查，如果不存在，用 os.mkdir() 创建
if not os.path.exists(target_path):
    os.mkdir('test_dir')
    print(f"成功创建目录: {target_path}")
else:
    print(f"目录已存在: {target_path}")
