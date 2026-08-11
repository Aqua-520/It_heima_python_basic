import os

# 1, 读取环境变量
# env = os.getenv('ARK_API_KEY')
# print(env)

# 2, 创建文件夹,在当前py程序文件的同级目录,默认
# os.mkdir('Huang_Yi_Ge')

# 3, 获取当前工作目录
# cwd = os.getcwd()
# print(cwd)

# 4, 切换工作目录
# os.chdir('Huang_Yi_Ge')
# cwd = os.getcwd()
# print(cwd)

# 5, 删除目录
# os.rmdir('Huang_Yi_Ge')

# 6, 删除文件
# os.remove('resources/你好小黄.txt')

# 7. 列出目录下的子文件或者子目录
# current_dir_list = os.listdir('./')
# print(current_dir_list)

# 8. 如果新旧路径在同一个目录下（如你的示例 resources/demo.html -> resources/demo666.html），
# 它仅仅是单纯的重命名，并没有跨目录剪切；
# 如果新旧路径在不同目录下（如 resources/demo.html -> data/demo.html），它才会起到剪切并重命名的作用。
# os.rename('resources/demo.html', 'resources/demo666.html')

# 9, path对象
# 路径拼接
path_join = os.path.join('resources', 'demo666.html')
print(path_join)

# 判断是判断是文件夹还是文件
print(os.path.isdir('resources'))
print(os.path.isfile('resources'))

# 获取文件的绝对路径
# 此绝对路径函数需要传递查哪个文件的绝对路径,需要先拿到文件路径
print(os.path.abspath(path_join))

# 判断目录是否存在
print(os.path.exists('./data'))
if not os.path.exists('data'):
    os.mkdir('./data')

# 路径拆分
print(os.path.split('wcy/speak.txt'))
