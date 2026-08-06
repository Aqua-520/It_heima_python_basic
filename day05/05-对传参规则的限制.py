# /之前的必须使用位置传参 *之后的必须使用关键字传参
def hello(s1,/,s2):
    print(s1+s2)

hello('yes',s2='lalalal')