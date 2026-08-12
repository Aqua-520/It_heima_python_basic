import os

# 假设当前目录下有一个名为 "old_name.txt" 的文件
old_filename = "./test_dir/old_name.txt"
new_filename = "./test_dir/new_name.txt"

# 1. 检查 old_filename 是否存在，如果存在则将其重命名为 new_filename
# TODO: 使用 os.path.exists() 和 os.rename()

# 如果在当前工作目录下找到了old_filename的文件 则进行改名操作
if os.path.exists(old_filename):
    # 使用rename方法更名称,如果是同级目录执行改名,如果非同级目录则执行剪切操作
    os.rename(old_filename, new_filename)
    print(f"成功将 {old_filename} 重命名为 {new_filename}")
else:
    print(f"未找到文件 {old_filename}")
    # 不存在则创建文件
    # 需要使用open方法
    file = open(f'{old_filename}', 'w', encoding='utf-8')
    file.write('随便写入的东西')
    # 关闭文件对象
    file.close()
