
import time
import functools


def logging(level):
    def func(foo):
        def wrapper(*args, **kwargs):
            start = time.time()
            print("[{level}]:enter function {foo}()".format(level=level, foo=foo.__name__))
            print(foo(*args, **kwargs))
            end = time.time()
            result = end - start
            return f"共计：{result}秒"
        return wrapper
    return func


@logging(level="INFO")
def foo(*args, **kwargs):
    num = functools.reduce(lambda i, j: i + j, range(100001))
    return num


@logging(level="DEBUG")
def do(something):
    print("do {}>>>".format(something))


if __name__ == "__main__":
    foo("hello")
    do("my work")
    logging("INFO")


# 类装饰器


class Logging(object):
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        def wapper(*args, **kwargs):
            start = time.time()
            print(func())
            end = time.time()
            result = end - start
            print(f"共计{result}秒")

        return wapper


@Logging(level="INFO")
def sun(*args, **kwargs):
    num = functools.reduce(lambda i, j: i + j, range(1000001))
    return num


if __name__ == "__main__":
    sun()


import time


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print("used:", end-start)
        return wrapper


@timeit
def foo():
    print("in foo()", foo())