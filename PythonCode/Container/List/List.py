# .insert(index, 数据)
# .append(数据)
# .extend(Iterable)
# remove
# clear()
# .reverse()

# .join(list)
list1 = ["春花秋月何时了", "往事知多少", "小楼昨夜又东风", "任尔东西南北风"]
str1 = " ".join(list1)
print(str1)

"""range:列表", "xrange：生成器", "linux:split"""
print("range:列表", "xrange：生成器", "linux:split")

for i in range(5, 0, -1):
    print(i)


l = []
for i in range(10):
    l.append({"num": i})
print(l)
# [{'num': 0}, {'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}, {'num': 7}, {'num': 8}, {'num': 9}]

ll = []
a = {"num": 0}
for i in range(10):
    a["num"] = i
    ll.append(a)
print(ll)
# >> [{'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}]

# 列表逆转
a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for j in range(len(a_list)):  # j =0
    for i in a_list:  # i = [1, 2, 3]
        print(i[j])

# a_list.reverse()  # 列表逆转一
# print(a_list)

# print(a_list[::-1])  # 列表逆转二

print(list(reversed(a_list)))  # 列表逆转三


datalist = [21, 'python', 'java', 'javascript', 34, 'hello world']
datalist[1:2] = 'only'
datalist[1:3] = ['day']
print(datalist)
print(datalist[1:3])