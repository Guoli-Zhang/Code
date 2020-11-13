
"""请按 alist 中元素的 age 由大到小排序"""
# alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
#
#
# def sort_by_age(list1):
#     return sorted(list1, key=lambda x: x["age"], reverse=True)
#
# print(sort_by_age(alist))


# 二维列表转置
"""[[1, 2, 3], [4, 5, 6], [7, 8, 9]] >> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]"""
a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [i for i in a_list]
print([[i[j] for i in a_list] for j in range(len(a_list[0]))])

alist = ["a", 'b', 'c', 'd', 'e', 'f']
blist = ['x', 'y', 'z', 'e', 'f']

alist.extend(blist)
alist = sorted(set(alist), key=alist.index, reverse=True)
print(alist)

