# 根据用户输入的内容进行三种条件判断

user_name = input('请输入是哪一位用户')

user_name_dict = [
    '黄一个',
    'xukinbei',
    '高市早苗'
]

if user_name == user_name_dict[0]:
    print('输入正确，当前登录用户：%s'% user_name)
elif user_name == user_name_dict[1]:
    print('输入正确，当前登录用户：%s' % user_name)
elif user_name == user_name_dict[2]:
    print('输入正确，当前登录用户：%s' % user_name)
else:
    print('你不是我们公司的人吧，你是哪来的间谍')