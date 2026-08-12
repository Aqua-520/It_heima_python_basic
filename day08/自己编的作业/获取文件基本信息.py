import os

filepath = "/users/documents/reports/2026_summary.txt"
# 提取的路径可以不存在,本质上是字符串操作

# 1. 提取路径中的文件名（带扩展名，例如 "2026_summary.txt"）
# TODO: 使用 os.path.basename()
filename = os.path.basename(filepath)
# print(filename)

# 2. 提取路径中的父目录路径（例如 "/users/documents/reports"）
# TODO: 使用 os.path.dirname()
dirname = os.path.dirname(filename)

# 3. 将文件名和扩展名分离（例如拆分成 "2026_summary" 和 ".txt"）
# TODO: 使用 os.path.splitext()
name_only, ext = os.path.splitext(filename)

print(f"文件名: {filename}")
print(f"目录路径: {dirname}")
print(f"主文件名: {name_only}, 后缀: {ext}")
