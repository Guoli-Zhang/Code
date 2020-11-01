"""
正确使用闭包，就要确保引用的局部变量在函数返回后不能变，改写以下程序，让它正确返回能计算1x1、2x2、3x3的函数。
"""


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()


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