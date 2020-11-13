# 有一组列表，请将列表中正数的平均值求出来。
# number = [-2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
# number_list = []
# result = 0
# for i in range(len(number)):
#     if number[i] > 0:
#         result += number[i]
#         number_list.append(number[i])
# a = result / len(number_list)
# print(a)

# 写出一段python代码实现一个删除一个list里面重复的元素。
# list = []
# new_list = [i for i in list if i not in list]

# 定义一个Fibonacci数列生成器的函数。
# def fun(n):
#     return n if n < 2 else fun(n - 2) + fun(n - 1)
#
#
# result = fun(20)
# print(result)

# def fibonacci(i):
#     fibonacci_list = []
#     for i in range(i):
#         fibonacci_list.append(1) if i < 2 else fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])
#
#
# fibonacci(20)


# python的参数传递是值传递还是引用传递？
# 引用传递

# 写下面的代码输出什么内容？
# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])
# print(list[3])

# 说出下面list1,list2,list3的输出值
# def extendList(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
# print("list1 = % s" % list1)
# print("list2 = % s" % list2)
# print("list3 = %s" % list3)
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# 简述with方法打开处理文件帮我们做了什么？
# 打开文件、编辑、关闭文件

# 下面两句代码有什么区别？
# a = [x for x in range(1, 100)]
# print(a)
# b = (x for x in range(1, 100))
# print(tuple(b))

# 有两个字典，a = {1:3，9:6},b = {2:5, 8:7},合并两个字典，并按value值升序排序。
# a = {1: 3, 9: 6}
# b = {2: 5, 8: 7}
# c = {}
# c.update(a)
# c.update(b)  # 建字典
# c.items()  # 返回的是： dict_items([('键', 值), ('键', 值), ('键', 值)])
# c_order = sorted(c.items(), key=lambda x: x[1], reverse=False)  # 字典的值传递给key,然后排列，x=('键', 值)。
# print(c_order)
# print(sorted(c.items(), key=lambda x: x[1], reverse=False))

# c = {}
# c.update(a)
# c.update(b)
# d = list(c.items())
# d.sort(key=lambda x: x[1], reverse=False)
# print(d)

# 写一段代码得到一个100以内的偶数列表（用你认为最简洁的方式)
# print([i for i in range(101) if i % 2 == 0])

# 统计一下字符串中每个字符出现的次数，并反向输出字符串每个字符。
# s3 = 'kjalfj;ldsjafl;hdslifdhg;lahfbl;hl;ahlf;h'
# s3_dict ={}
# for i in s3:
#     s3_dict[i] = s3.count(i)
# s1 = str(s3_dict)
# print(s1[1:len(s1) - 1])
# print(s3[::-1])

# def strcount(a):
#     #定义一个空字典
#     b = {}
#     # 求出字符串的长度
#     for i in range(len(a)):
#         if a[i] in b:
#             b[a[i]] += 1
#         else:
#             b[a[i]] = 1
#     #遍历字典
#     for item in b.items():
#         print(item)
# if __name__ == '__main__':
#     a="kjalfj;ldsjafl;hdslifdhg;lahfbl;hl;ahlf;h"
#     strcount(a)


# 有两个序列a, b, 大小都为n,序列元素的值任意整形数，无序；要求：
# 通过交换a,b中的元素，使【序列a元素的和】与序列b元素的和】之间的差最小。
# a = [5, 6, 7, 8, 7, 4, 7, 221]
# b = [34, 54, 67, 2, 3, 11, 24]
# import random
# import time
#
#
# def timeit(func):
#     def _deco(*args, **kwargs):
#         start = time.clock()
#         d = func(*args, **kwargs)
#         end = time.clock()
#         print(f"used time:{str(end - start)}")
#         return d
#
#     return _deco
#
#
# @timeit
# def exchange(a_list, b_list):
#     sum_a = sum(a_list)
#     sum_b = sum(b_list)
#     d = abs(sum_a - sum_b)
#     if d == 0:
#         return d
#     b_exchange = False
#     for index_a, value_a in enumerate(a_list):
#         if d == 0:
#             break
#         for index_b, value_b in enumerate(b_list):
#             temp_d = abs((sum_a - value_a + value_b) - (sum_b + value_a - value_b))
#             if temp_d < d:
#                 b_exchange = True
#                 temp_index_a = index_a
#                 temp_index_b = index_b
#                 d = temp_d
#                 if b_exchange:
#                     sum_a = sum_a - a_list[temp_index_a] + b_list[temp_index_b]
#                     sum_b = sum_b - b_list[temp_index_b] + a_list[temp_index_a]
#                     temp_v = a_list[temp_index_a]
#                     a_list[temp_index_a] = b_list[temp_index_b]
#                     b_list[temp_index_b] = temp_v
#                     b_exchange = False
#     return d
#
#
# a_list = []
# b_list = []
# for i in range(1000):
#     a_list.append(random.randint(0, 1000000))
# for i in range(1000):
#     b_list.append(random.randint(0, 1000000))
# print(exchange(a_list, b_list))
# a_list = []
# b_list = []
# for i in range(10000):
#     a_list.append(random.randint(0, 1000000))
# for i in range(10000):
#     b_list.append(random.randint(0, 1000000))
# print(exchange(a_list, b_list))

# 现在有一张会员表，量级在千万级以上，每个会员都有一个积分字段（整数型），现在想将该会员表会员划分
# A,B,C,D四个会员等级，A会员比例不得超过积分排名前5%，B会员比例不得超过前20%，C级不得超过前40%，余下为D级会员，
# 该如何划分？

list1 = [{"a": 20}, {"b": 21}, {"c": 16}, {"d": 50}, {"e": 10}, {"f": 30}, {"g": 60}, {"h": 40}, {"i": 80}]
A_list = []
len(A_list)

