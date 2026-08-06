def fn1():
    print('1')
    fn2()
    print('5')

def fn2():
    print('2')
    fn3()
    print('4')

def fn3():
    print('3')

fn1()