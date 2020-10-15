# encoding:utf-8

"""希尔排序"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            j = i
            while (j - gap) >= 0:
                if alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(blist)
    shell_sort(blist)
    print(blist)
