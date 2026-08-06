# ============================================================================
# 练习1：智能数据筛选器
# ============================================================================
#
# 题目描述：
#   请设计一个通用数据筛选函数 filter_data，要求功能如下：
#   1. 通过 *args 接收任意数量的数值数据
#   2. 通过 **kwargs 接收筛选配置，支持的配置项包括：
#      - threshold：阈值，只保留大于等于该值的数据（默认：无阈值）
#      - top_n：只保留前N个（默认：全部保留）
#      - unique：是否去重（默认 False）
#      - sort_order：排序方式，"asc" 升序 / "desc" 降序（默认 "asc"）
#   3. 为所有函数添加完整的类型注解
#
#   测试：
#     filter_data(5,2,9,1,7,3,8,2,9,4, threshold=5, unique=True, sort_order="desc")
#       → [9, 8, 7, 5]
#     filter_data(3,5,1,8,6, top_n=3)
#       → [1, 3, 5]
# ============================================================================


# 定义筛选函数
def my_filter(*args,**kwargs):
    # 四个默认配置对象
    defaul_options = {
        # 阈值，只保留大于等于该值的数据（默认：无阈值）
        "threshold" : None,
        # 只保留前N个 （默认：全部保留）
        "top_n" : None,
        # unique：是否去重（默认 False）
        "is_unique" : False,
        # 排序方式，"asc" 升序 / "desc" 降序（默认 "asc"）
        "sort_order" : "asc"
    }
    # 通过update方法对默认配置进行覆盖和更新
    defaul_options.update(kwargs)

    # args用来接收复数个数值数据,kwargs用来接收配置对象
    result_list = [item for item in args]

    # 阈值拦截
    if not defaul_options["threshold"] is None:
        # 如果配置参数不是null
        result_list = [num for num in result_list if num >= defaul_options["threshold"]]

    
