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
        "unique" : False,
        # 排序方式，"asc" 升序 / "desc" 降序（默认 "asc"）
        "sort_order" : "asc"
    }
    # 通过update方法对默认配置进行覆盖和更新
    defaul_options.update(kwargs)

    # args用来接收复数个数值数据,kwargs用来接收配置对象
    result_list = [item for item in args]

    # 第一步先去重
    # 是否去重
    if defaul_options["unique"]:
        current_set = set(result_list)
        result_list = list(current_set)

    # 第二步阈值拦截
    # 阈值拦截
    if not defaul_options["threshold"] is None:
        # 如果配置参数不是null
        result_list = [num for num in result_list if num >= defaul_options["threshold"]]

    # 第三步排序
    # 排序方式 是倒叙则将反转设置为True
    result_list.sort(reverse=(defaul_options.get('sort_order') == "desc"))

    # 最后返回指定几个
    # top_n：只保留前N个
    if defaul_options["top_n"] is not None:
        # 不是not则进行配置应用
        result_list = result_list[:defaul_options["top_n"]] # 从开头切片到第n个




    # 最终返回结果
    return  result_list

print("测试 1:", my_filter(5, 2, 9, 1, 7, 3, 8, 2, 9, 4, threshold=5, unique=True, sort_order="desc"))
# 预期输出: [9, 8, 7, 5]

# 定义配置项字典
user_options = {
        # 保留大于等于多少的数
        "threshold" : 0,
        # 只保留前N个
        "top_n" : 10,
        # unique：是否去重
        "unique" : True,
        # 排序方式，"asc" 升序 / "desc" 降序
        "sort_order" : "asc"
}
# 原始数据
origin_data_list = [-10, 0, 5, 20, 30, 40, 50, 10, 30, 50, 60, 25, 99.5, 100, 100, 0, -5, 88, 40, 72]
print(my_filter(*origin_data_list,**user_options))