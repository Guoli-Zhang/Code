# encoding:utf-8


def my_function(func):

    a = 100
    b = 200
    # 把 cucalate_rule 当做函数来调用
    result = func(a, b)
    print('result:', result)


my_function(lambda a, b: a / b)
my_function(lambda a, b: a // b)
my_function(lambda a, b: a % b)


# ---
import functools
list2 = []
list2.append(functools.reduce(lambda i, j: j**3 - i**3, range(2)))
print(list2)



