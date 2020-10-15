# encoding:utf-8

"""二分法"""


def binary_search(alist, item):
    """
    二分查找，递归实现版本
    :param alist: 查找列表
    :param time: 查找元素
    :return: True False
    """
    n = len(alist)
    mid = n // 2
    if 0 == n:
        return False
    if alist[mid] == item:
        return True
    if item < alist[mid]:
        return binary_search(alist[:mid], item)
    else:
        return binary_search(alist[mid+1:], item)


def binary_search2(alist, item):
    """
    二分查找，非递归版本
    :param alist:
    :param item:
    :return: True False
    """
    start = 0
    end = len(alist) - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(binary_search(blist, 0))
    print(binary_search2(blist, 0))
    print(binary_search(blist, 31))
    print(binary_search2(blist, 31))
