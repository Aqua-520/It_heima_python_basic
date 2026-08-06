# 默认参数也称为缺省参数，用于在定义函数时，为参数提供默认值，
# 调用函数时，可以不传递有默认值的参数。注意：默认值参数只能放在普通参数的后面

def default_params(name,age=18):
    # age加默认参数的时候，不允许将形式参数的定义放在别的参数之前
    print(
        f"用户姓名：{name},年龄：{age}"
    )
    return None

default_params('王大帅')