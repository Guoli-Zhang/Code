# -*- coding:utf-8 -*-

# 最小公倍数
from random import randint

a, b = randint(1, 1000), randint(1, 1000)
print(a, b)

import math  # python3

# print(math.gcd(a, b)) 最大公约数
print(a * b / math.gcd(a, b))

from fractions import _gcd  # python2

print(a * b / _gcd(a, b))


def soultion(a, b):
    max_num, min_num = max(a, b), min(a, b)
    for i in range(1, min_num + 1):
        if max_num * i % min_num == 0:
            print(i)
            return max_num * i


def gcd(a, b):
    if a < b:
        a, b = b, a
    temp = a % b
    if temp == 0:
        return b
    else:
        return gcd(temp, b)


def gcy(a, b):
    temp = gcd(a, b)
    return a * b / temp


if __name__ == "__main__":
    soultion = soultion(a, b)
    temp = gcy(a, b)
    print(f"{soultion}\n{temp}")

# ^ 运算
a = 2
b = 3
a = a ^ b
print(a)

b = b ^ a
print(b)

a = a ^ b
print(a)

# def feibo(num):

e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原数列：e={e}\n索引为奇数的数列：f={e[::2]}\n索引为偶数的数列：h={e[1::2]}")
f = []
h = []


def fun(e):
    for index in range(len(e)):
        if index % 2 == 0:
            f.append(e[index])
        else:
            h.append(e[index])
    return f, h


e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = fun(e)
print(k)


