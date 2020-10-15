# encoding:utf-8

my_list = [1, 2, 3, 4, 5]


def f(x):
    return x ** 2


result = map(f, my_list)
print(type(result), result, list(result))


# ---

my_list = ['smith', 'edward', 'john', 'obama', 'tom']


def f(x):
    return x[0].upper() + x[1:]


result = map(f, my_list)
print(list(result))

import numpy

print(list(map(lambda x , y: x + y, range(20), range(10))))
print([x + y for x, y in zip(range(20), range(10))])
print(list(numpy.array(range(10)) + numpy.array(range(10))))

v1 = [21, 34, 45]

v2 = [55, 25, 77]

v = list(map(lambda x: x[0]-x[1], zip(v2, v1)))

print(v)

