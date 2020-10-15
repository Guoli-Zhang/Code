# 生成器

# <class 'generator'>
x = (x for x in range(10))
print(f"{x}\n{type(x)}")


# # create a generator
def createGenerator():
    mylist = range(4)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # create a generator
print(mygenerator)  # mygenerator is an generator object
for i in mygenerator:
    print(i)

# >> [0, 2, 4, 6]
def multipliers():
    # return [lambda x: i * x for i in range(4)]
    # return [lambda x, i=i: i * x for i in range(4)]
    for i in range(4):
        yield lambda x: i * x


print([m(2) for m in multipliers()])


def func(values):
    for value in values:
        print(f"func:{value}")
        yield value


import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield
        a, b = b, a + b
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

# def triangle():
#     _list, new_list = [], []
#     while True:
#         length = len(_list)
#         if length == 0:
#             new_list.append(1)
#         else:
#             for times in range(length + 1):
#                 if times == 0:
#                     new_list.append(1)
#                 elif times == length:
#                     new_list.append(1)
#                 else:
#                     times = _list[times - 1] + _list[times]
#                     new_list.append(times)
#         yield new_list
#         _list = new_list.copy()
#         new_list.clear()
