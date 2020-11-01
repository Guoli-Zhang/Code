def count():
    fs = []
    for i in range(1, 4):
        def lazy_count(j):
            def cou():
                return j * j

            return cou

        r = lazy_count(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

import time
from functools import wraps


def performance(func):
    # 使用wraps, 保证被装饰过的函数__name__的属性不变
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("the {} running time is {}".format(func.__name__, (end_time - start_time)))
        return res

    return inner


def decorator(func):
    """this is decorator __doc__"""

    def wrapper(*args, **kwargs):
        """this is wrapper __doc__"""
        print("this is wrapper method")
        return func(*args, **kwargs)

    return wrapper


@decorator
def test():
    """this is test __doc__"""
    print("this is test method")


print("__name__: ", test.__name__)
print("__doc__:  ", test.__doc__)
"""
结果：
__name__:  wrapper

__doc__:   this is wrapper __doc__
"""

from functools import wraps


def decorator(func):
    """this is decorator __doc__"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """this is wrapper __doc__"""
        print("this is wrapper method")
        return func(*args, **kwargs)

    return wrapper


@decorator
def test():
    """this is test __doc__"""
    print("this is test method")


print("__name__: ", test.__name__)
print("__doc__:  ", test.__doc__)
"""
结果：
__name__:  test

__doc__:   this is test __doc__

"""
