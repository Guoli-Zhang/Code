# encoding:utf-8

import functools

lista = [1, 2, 3, 4, 5, 6, 7]
result = functools.reduce(lambda i, j: i + j, lista)
print(result)

# ---
list2 = []
list2.append(functools.reduce(lambda i, j: j**3 - i**3, range(2)))
print(list2)


def Sum(*args):
    count = 0
    for i in args:
        count += i
    return count


def main():
    sum = 0  # 定义变量做累加器
    n = int(input('n='))  # 从键盘上输入累加的范围
    for x in range(n):
        sum += (x + 1)
    print(sum)


def sum_numbers(num):
    # 1.出口
    if num == 1:
        return 1

    # 2.数组累加
    temp = sum_numbers(num - 1)
    print(temp)
    print(num)
    return num + temp


result = sum_numbers(3)
print(result)


if __name__ == '__main__':
    main()

# ---

my_list = [1, 2, 3, 4, 5]


def f(x1, x2):
    return x1 + x2


result = functools.reduce(f, my_list)
print(result)
