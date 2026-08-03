# 引导用户输入两个数字,将两个数的输入进行加减乘除,打印到控制台
input1 = int(input('请输入第一个自然数'))
input2 = int(input('请输入第二个自然数'))

sum_result = input1 + input2
sub_result = input1 - input2
mul_result = input1 * input2
# 带小数的除法
div_result = input1 / input2

print(sum_result,sub_result,mul_result,div_result)