def fun1(*args, a=10, b=20, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


fun1(5, 4, a=12, b=10, c='8', d='6')


def fun2(*args):
    result = 0
    for i in args:
        result += i
    print(result)


fun2(5, 6, 7, 0)


def fun3(**kwargs):
    print(kwargs)


fun3(name="mks", QQ="13456")


