
list1 = [1, 2, 3]
list2 = [3, 4, 5]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)  # &：求同
print(set1 ^ set2)  # ^：求异

# 请写出一段 Python 代码实现删除一个 list 里面的重复元素?
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))
print(l2)

l3 = l2.sort(key=l1.index)
print(l3)
# >> None

l4 = sorted(set(l1), key=l1.index)
print(l2)
