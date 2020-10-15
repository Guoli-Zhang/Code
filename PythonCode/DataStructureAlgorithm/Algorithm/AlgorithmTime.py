# encoding:utf-8

"""排序算法用时比较"""
# -*- coding: UTF-8 -*-
# Space:https://github.com/Tri-x/exercise
# Space:https://space.bilibili.com/187492698
# Author:Trix
# Description:排序算法
# Python的排序算法用的是Time Sort 一种源自归并排序和插入排序的稳定高效的排序算法

from random import randint  # 随机整数
from time import process_time  # 计时

nums_lists = [[] for n in range(4)]  # 随机创建四个无序数列，用来粗略地测试每种排序算法的用时
for n in range(500):  # 数列长度为500
    nums_lists[0].append(randint(-400, 400))  # 随机范围：（-400, 400）
for n in range(1000):
    nums_lists[1].append(randint(-8000, 8000))
for n in range(5001):
    nums_lists[2].append(randint(-2000, 2000))
for n in range(10000):
    nums_lists[3].append(randint(-9000, 9000))


def bubble_sort(num_list):  # 冒泡排序
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


def select_sort(num_list):  # 选择排序
    for i in range(len(num_list) - 1):
        min_index = i
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[min_index]:
                num_list[min_index], num_list[j] = num_list[j], num_list[min_index]
    return num_list


def insert_sort(num_list):  # 插入排序
    for i in range(1, len(num_list) + 1):
        for j in range(i):
            if i < len(num_list):
                if num_list[i] <= num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


def shell__sort(num_list):
    gap = len(num_list) // 2
    while gap >= 1:
        for j in range(gap, len(num_list)):
            while (j - gap) >= 0:
                if num_list[j] < num_list[j - gap]:
                    num_list[j], num_list[j - gap] = num_list[j - gap], num_list[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return num_list


def merge_sort(num_list):  # 归并排序
    if len(num_list) <= 1:
        return num_list
    middle = len(num_list) // 2
    list_before = merge_sort(num_list[:middle])
    list_after = merge_sort(num_list[middle:])
    return merge_compare(list_before, list_after)


def merge_compare(list_before, list_after):
    result_list = []
    before_index = after_index = 0
    while before_index < len(list_before) and after_index < len(list_after):
        if list_before[before_index] < list_after[after_index]:
            result_list.append(list_before[before_index])
            before_index += 1
        elif list_after[after_index] <= list_before[before_index]:
            result_list.append(list_after[after_index])
            after_index += 1
    if before_index == len(list_before):
        for i in list_after[after_index:]:
            result_list.append(i)
    elif after_index == len(list_after):
        for i in list_before[before_index:]:
            result_list.append(i)
    return result_list


def quick_sort(num_list):  # 快速排序
    quick_recursion(num_list, 0, len(num_list) - 1)


def quick_recursion(num_list, head_index, tail_index):
    if head_index < tail_index:
        pivot_index = quick_partition(num_list, head_index, tail_index)
        quick_recursion(num_list, head_index, pivot_index - 1)
        quick_recursion(num_list, pivot_index + 1, tail_index)
    return num_list


def quick_partition(num_list, head_index, tail_index):
    pivot = num_list[tail_index]
    exchange_index = head_index - 1
    for i in range(head_index, tail_index):
        if num_list[i] < pivot:
            exchange_index += 1
            num_list[exchange_index], num_list[i] = num_list[i], num_list[exchange_index]
    num_list[exchange_index + 1], num_list[tail_index] = num_list[tail_index], num_list[exchange_index + 1]
    return exchange_index + 1


def heap_sort(num_list):  # 堆排序
    list_len = len(num_list)
    for i in range(list_len // 2, -1, -1):
        heapify(num_list, list_len, i)
    for i in range(list_len - 1, 0, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        list_len -= 1
        heapify(num_list, list_len, 0)
    return num_list


def heapify(num_list, list_len, parent_index):
    left_index = 2 * parent_index + 1
    right_index = left_index + 1
    max_index = parent_index
    if left_index < list_len and num_list[left_index] > num_list[max_index]:
        max_index = left_index
    if right_index < list_len and num_list[right_index] > num_list[max_index]:
        max_index = right_index
    if max_index != parent_index:
        num_list[parent_index], num_list[max_index] = num_list[max_index], num_list[parent_index]
        heapify(num_list, list_len, max_index)


def count_sort(num_list):  # 计数排序
    max_num = max(num_list)
    min_num = min(num_list)
    neg_list = []
    pos_list = []
    for num in num_list:
        if num < 0:
            neg_list.append(num)
        if num >= 0:
            pos_list.append(num)
    if len(neg_list) != 0:
        neg_counts_list = [0 for i in range(min_num, 0)]
        for i in range(len(neg_list)):
            neg_counts_list[neg_list[i]] += 1
        neg_index = 0
        for i in range(-len(neg_counts_list), 0):
            while neg_counts_list[i] > 0:
                neg_list[neg_index] = i
                neg_index += 1
                neg_counts_list[i] -= 1
    if len(pos_list) != 0:
        pos_counts_list = [0 for i in range(max_num + 1)]
        for i in range(len(pos_list)):
            pos_counts_list[pos_list[i]] += 1
        pos_index = 0
        for i in range(len(pos_counts_list)):
            while pos_counts_list[i] > 0:
                pos_list[pos_index] = i
                pos_index += 1
                pos_counts_list[i] -= 1
    result_list = neg_list + pos_list
    return result_list


def bucket_sort(num_list):  # 桶排序
    bucket_list = [0 for i in range(max(num_list) - min(num_list) + 1)]
    for i in range(len(num_list)):
        bucket_list[num_list[i] - min(num_list)] += 1
    result_list = []
    for i in range(len(bucket_list)):
        if bucket_list[i] != 0:
            result_list += [i + min(num_list)] * bucket_list[i]
    return result_list


def radix_sort(num_list):  # 基数排序
    pos_list = []
    neg_list = []
    for num in num_list:
        if num < 0:
            neg_list.append(num)
        if num >= 0:
            pos_list.append(num)
    if len(neg_list) != 0:
        neg_num_digit = 0
        while neg_num_digit < len(str(min(neg_list))):
            neg_values_lists = [[] for i in range(10)]
            for neg_num in neg_list:
                neg_values_lists[int(neg_num / (10 ** neg_num_digit)) % 10].append(neg_num)
            neg_list.clear()
            for neg_value_list in neg_values_lists:
                for neg_num in neg_value_list:
                    neg_list.append(neg_num)
            neg_num_digit += 1
    if len(pos_list) != 0:
        pos_num_digit = 0
        while pos_num_digit < len(str(max(pos_list))):
            pos_values_lists = [[] for i in range(10)]
            for pos_num in pos_list:
                pos_values_lists[int(pos_num / (10 ** pos_num_digit)) % 10].append(pos_num)
            pos_list.clear()
            for pos_value_list in pos_values_lists:
                for pos_num in pos_value_list:
                    pos_list.append(pos_num)
            pos_num_digit += 1
    result_list = neg_list + pos_list
    return result_list


# 记录每一种排序算法对于不同长度无序数列的排序时间
sorts_time_dict = {
    bubble_sort: ["Bubble Sort"],  # 冒泡排序
    select_sort: ["Select Sort"],  # 选择排序
    insert_sort: ["Insert Sort"],  # 插入排序
    shell__sort: ["Shell Sort"],  # 希尔排序
    merge_sort: ["Merge Sort"],  # 归并排序
    quick_sort: ["Quick Sort"],  # 快速排序
    heap_sort: ["Heap Sort"],  # 堆排序
    count_sort: ["Count Sort"],  # 计数排序
    bucket_sort: ["Bucket Sort"],  # 桶排序
    radix_sort: ["Radix Sort"]  # 基数排序
}

for num_list in nums_lists:  # 由于两层for循环会使对数列进行快速排序时递归太深，会引起python崩溃,单独对每个数列进行排序
    print("正在对第"+str(nums_lists.index(num_list)+1)+"个长为"+str(len(num_list))+"的随机数列执行Quick Sort算法")
    start_time = process_time()  # 开始计时，计时部分为排序算法
    quick_sort(num_list)
    end_time = process_time()  # 结束计时
    sorts_time_dict[quick_sort].append(end_time - start_time)  # 记录每种排序算法对不同长度数列的排序时间 单位为秒
for num_list in nums_lists:  # 对每一个数列进行每一种排序算法
    for func_sort, time_list in sorts_time_dict.items():
        if func_sort != quick_sort:
            print("正在对第" + str(nums_lists.index(num_list) + 1) + "个" + "长为"
                  + str(len(num_list)) + "的随机数列执行" + time_list[0] + "算法", )
            start_time = process_time()  # 开始计时，计时部分为排序算法
            func_sort(num_list.copy())  # 排序算法 .copy() 复制品 防止改变原数列
            end_time = process_time()  # 结束计时
            time_list.append(end_time - start_time)  # 记录每种排序算法对不同长度数列的排序时间 单位为秒
print(" ")
print("十种排序算法对于不同长度的随机无序数列的排序时间结果如下：")
print("{:20s}{:<15d}{:<15d}{:<15d}{:<15d}".format("Length of Series:", 500, 1000, 5001, 10000))  # 格式化输出
for time_list in sorts_time_dict.values():  # 每种算法
    for sort_time in time_list:  # 每种算法的名称和其处理每个数列的时间
        if not isinstance(sort_time, float):  # 如果use_time类型不为float 即为名称
            print("{:20s}".format(sort_time + ":"), end=" ")
        else:
            print("{:<15.4f}".format(sort_time), end=" ")  # 左对齐，保留四位小数
    print(" ")
print("单次随机数列排序时间结果不代表所有")
print(" ")
count_sort_list = []  # 因为计数排序太快了，单独创建一个长度为100000的数列来测试排序时间
for i in range(100000):
    count_sort_list.append(randint(-80000, 100000))
start_time_count_sort = process_time()  # 开始计时，计时部分为排序算法
count_sort(count_sort_list.copy())
end_time_count_sort = process_time()  # 结束计时
print("计数排序一个长度为100000的随机数列所用的时间为" + str(round(end_time_count_sort - start_time_count_sort, 3)) + "秒")
