# 导入软件包目录下的模块需要多加一个点
# import utils.my_var
#
# # 使用变量
# print(utils.my_var.name)
#
# # 通过from解一层
# from utils import my_var,my_log
#
# my_log.log1()
#
# # 通过from解两层层
# from utils.my_var import name,age
#
# print(name)
# print(age)

# 通过*号导入软件包下所有模块
from utils import *

# 导入软件包当中的模块,需要先在init入口文件进行初始化声明
my_log.log1()
print(my_var.name)

# 定位到模块,直接通过*拿到模块内的所有变量
from utils.my_var import *

print(name, age)
