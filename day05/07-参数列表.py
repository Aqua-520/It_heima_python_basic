def calc_data(*args,**kwargs):
    # 不定长参数
    # 不定长参数会在调用时,将实参打包成元组传递进函数体当中
    # 函数体可以通过遍历的方式使用元组的每一个值
    min_value = min(args)
    max_value = max(args)
    avg_value = sum(args) / len(args)

    # 两个**接收关键字参数,将函数调用时的关键字传参打包成对象传递进函数体
    if kwargs.get('is_print') and kwargs['is_print']:
        print('是否打印配置项位True,执行打印')
        print(f'最大值{max_value},最小值{min_value},平均值{avg_value}')

    return min_value,max_value,avg_value

print(calc_data(1,2,3,4,5))
calc_data(2,2,3,4,5,6,7,8,is_print=True)