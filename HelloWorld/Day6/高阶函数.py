num_list = [1, 2, 3, 1, 5, 1, 0, 0, 8, 6]


# def f(x):
#     return x * 10


result = list(map(lambda x: x * 10, num_list))
print(result)


word = ["apple", "james", "rose", "enumerate", "print", "functions"]


def f(x):
    return x[0].upper() + x[1:]


result = list(map(f, word))
print(result)

words = ["Apple", "james", "Rose", "Enumerate", "print", "functions"]


def f(x):
    return x[0].isupper()


result = list(filter(f, words))
print(result)

num_list = [1, 10, 8, 9, 86]

import functools


def f(x1, x2):
    return x1 * x2


result = functools.reduce(f, num_list)
print(result)
