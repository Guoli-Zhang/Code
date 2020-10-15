# encoding:utf-8

"""冒泡排序"""


def bubble__sort(alist):
    """冒泡排序"""
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(0, n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if 0 == count:
            break


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(blist)
    bubble__sort(blist)
    print(blist)
