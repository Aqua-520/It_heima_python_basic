# 本文件位于: day06/模块路径测试/test01.py
# 目标: 访问上一级目录(day06)下的 utils 软件包中的模块

# 直接运行本文件时, Python 默认只把 "本文件所在目录" 加入搜索路径(sys.path),
# 因此找不到上一级的 utils 包.
# 解决办法: 用内置的 os / sys 把上一级目录(day06)加进搜索路径即可,
# 不需要安装任何第三方工具.

import os
import sys

# __file__ 是本文件的路径
# abspath  -> 转成绝对路径, 避免用相对路径运行时出错
# dirname  -> 往上退一层目录
# 套两次 dirname: test01.py 所在目录 -> day06 目录
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# 现在 day06 已在搜索路径中, 可以像在 day06 目录下一样导入 utils 包
from utils import my_log

my_log.log1()
