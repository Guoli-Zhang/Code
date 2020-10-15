
# [[0~10] * 10]
print([x * 11 for x in range(10)])

"""Python一行代码实现九九乘法表"""
print('\n'.join('   '.join(['%sX%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)))

"""[0~10]以索引分别打印奇偶数列表"""
a = [i for i in range(10)]
print(f"原数列：{a}\n偶数列：{a[::2]}\n奇数列：{a[1::2]}")

"""一行打印[[1, 2, 3]...[100, 101, 102]]"""
print([[x for x in range(1, 103)][i:i + 3] for i in range(0, 102, 3)])

# 二维列表转置
"""[[1, 2, 3], [4, 5, 6], [7, 8, 9]] >> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]"""
a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [i for i in a_list]
print([[i[j] for i in a_list] for j in range(len(a_list[0]))])

"""[1, 7, 19...28519, 29107, 29701]"""
list3 = [x**3 - (x-1)**3 for x in range(1, 101)]
print(list3)

import random
import cProfile


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i< 0.5]
    return [i * i for i in l2]


def f2(lIn):
    l1 = [i for i in lIn if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]


def f3(lIn):
    l1 = [i * i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i < (0.5 * 0.5)]


lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')


def a():
    alist = []
    for i in range(1, 100):
        if i % 6 == 0:
            alist.append(i)
    last_num = alist[-3:]
    return last_num


result = a()
print(result)

