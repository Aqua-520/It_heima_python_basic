# 捕获异常
try:
    num1 = int(input('请输入第一个数'))
    num2 = int(input('请输入第二个数'))

    # 结果是
    result = num1 / num2
    print(f"结果是:{result}")

    # 捕获除0异常和数值错误异常,ValueError,ZeroDivisionError
# except (ZeroDivisionError, ValueError) as e:
#     print('可以使用元组来根据不同的异常执行相同的处理逻辑')
#     print(e)

# 也可以多次匹配
except ZeroDivisionError as e:
    print('触发除0异常')
except ValueError as e:
    print('触发数值异常')
except Exception as e:
    print('触发统一的异常对象')

finally:
    print('finally无论如何都会执行')

# 被异常处理后,后续代码还能正确执行
print('后续代码正常执行')
