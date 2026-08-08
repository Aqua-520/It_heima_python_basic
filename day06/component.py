# 此文件为导出文件
# __all__ 限制对方在通过*导入我方的时候,暴露哪些变量给对方
__all__ = ['log_01',"PI","NAME"]

PI = 3.1415926
NAME = '黄一个'

log_01 = lambda : print('我是打印一号')
log_02 = lambda : print('我是打印二号')
log_03 = lambda : print('我是打印三号')
log_04 = lambda : print('我是打印四号')


print(__name__)
# 使用环境变量来进行分支区分
if __name__ == '__main__':
    # 在当前模块被执行的时候,内置__name__的属性为__main__
    # 如果被别的py模块导入,执行此模块的时候,环境变量会发生变化,变成模块名
    # 测试代码
    log_01()