def bubbleSort(array):
    """冒泡排序"""
    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return[array]


array1 = [2, 1, 5, 3, 8, 1, 2, 3, 9, 4, 2]
print(bubbleSort(array1))


def FindSmall(list):
    """找到最小元素"""
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min


def Select_Sort(list):
    """选择排序"""
    newArr = []
    for i in range(len(list)):
        minValue = FindSmall(list)
        newArr.append(minValue)
        list.remove(minValue)
    return newArr


testArr = [2, 5, 7, 1, 8, 3, 6, 9, 2]
print(Select_Sort(testArr))


def Quick_Sort(list):
    """快速排序"""
    if len(list) < 2:
        return list
    else:
        temp = list[0]
        less = [i for i in list[1:] if i <= temp]
        more = [i for i in list[1:] if i > temp]
        return Quick_Sort(less) + [temp] + Quick_Sort(more)


testArr = [13, 14, 12, 21, 5, 31, 11]
print(Quick_Sort(testArr))


# def Item_Search(list, item):
#     low = 0
#     high = len(list - 1)
#     while low <= high:
#         middle = (low + high) // 2
#         print(list[middle])
#         if list[middle] > item:
#             high = middle - 1
#         elif list[middle] < item:
#             low = middle + 1
#         else:
#             return middle
#     return None
#
#  test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# Item_Search(test_list, 11)


# 广度优先搜索
# graph = {}
# graph["you"] = ["Alice", "Bob", "Claire"]
# graph["Bob"] = ["Anuj", "peggy"]
# graph["Alice"] = ["Peggy"]
# graph["Claire"] = ["Tom", "Jonny"]
# graph["Anuj"] = []
# graph["Peggy"] = []
# graph["Tom"] = []
# graph["Jonny"] = []
# from collections import deque
# def person_is_seller(name):
#     return name == "Tom"
# def Search(name):
#     Searched = []
#     search_queue = deque()
#     search_queue += graph[name]
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in Searched:
#             if person_is_seller(person):
#                 print("ther seller is {0} ".format(person))
#                 return True
#             else:
#                 search_queue += graph[person]
#                 Searched.append(person)
#     return False
#
#
# print(Search("you"))


