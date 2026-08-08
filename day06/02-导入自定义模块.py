# 导入我写的component模块文件
import component

component.log_01()
component.log_02()
component.log_03()
component.log_04()

# 导入特定功能
from component import NAME,PI
print(NAME,PI)

from component import *
# 通过*导入的情况下,只能使用对方__all__规定导出的内容
log_01()

# 在我们使用导入模块的情况下,会先运行一遍模块文件,收集依赖
# 在模块文件中如果需要运行函数做测试的情况下,函数会被执行
# 导致我方调用对方模块内容的时候,对方的测试代码也会被执行