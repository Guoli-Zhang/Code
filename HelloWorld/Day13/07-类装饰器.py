class Func_out(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("这是内部函数！")
        self.__fn(*args, **kwargs)


@Func_out
def fun(*args, **kwargs):
    result = 0
    for value in args:
        result -= value
    for value in kwargs.values():
        result *= value
    print(result)


if __name__ == "__main__":
    fun(1, 2, 4, 6, 12, a=3, b=5, c=6)

