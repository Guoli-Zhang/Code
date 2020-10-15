# encoding:utf-8

"""归并排序"""


def merge_sort(alist):
    n = len(alist)
    if 1 == n:
        return alist
    mid = n // 2
    left_sort_list = merge_sort(alist[:mid])
    right_sort_list = merge_sort(alist[mid:])
    left, right = 0, 0
    merge_sort_list = []
    left_list_n = len(left_sort_list)
    right_list_n = len(right_sort_list)
    while left < left_list_n and right < right_list_n:
        if left_sort_list[left] <= right_sort_list[right]:
            merge_sort_list.append(left_sort_list[left])
            left += 1
        else:
            merge_sort_list.append(right_sort_list[right])
            right += 1
    merge_sort_list += left_sort_list[left:]
    merge_sort_list += right_sort_list[right:]
    return merge_sort_list


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(f"before_alist:{blist}")
    alist = merge_sort(blist)
    print(f"after_list:{blist}")
    print(f"fall_list:{alist}")
