# encoding:utf-8


"""选择排序"""


def select_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if i != alist[min_index]:
            alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(blist)
    select_sort(blist)
    print(blist)
