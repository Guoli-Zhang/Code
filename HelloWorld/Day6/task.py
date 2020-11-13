# def test1(a):
#     a = 200
#     print('test1--- %d'%a)
#
# data = 100 # data 是一个数字
# test1(data)
# print('main --- %d'%data)


# def test1(a):
#     a.append(22)
#     print('test1--- %s'%a)
#
# data = [11] # data 是一个列表
# test1(data)
# print('main --- %s'%data)


# def test1(a):
#     a = []
#     a.append(22)
#     print('test1--- %s'%a)
#
# data = [11] # data 是一个列表
# test1(data)
# print('main --- %s'%data)


# def fun1(*args, a, b, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
#
# fun1(40, 50, a=10, b=20, c="cc", d="dd")


# def num(a, b):
#     list1 = [a, b]
#     return max(list1)
#
#
# result = num(10, 26)
# print(result)
#
#
# def num(a, b):
#     list1 = [a, b]
#     return min(list1)
#
#
# result = num(10, 26)
# print(result)


# def fun1(par1):
#     print(par1)
#
#
# def fun2():
#     print("我是fun2")
#     # 函数嵌套：某个函数中，调用某个函数
#     fun1("asd")
#


# def sum(a, b):
#     num1 = a
#     num2 = b
#     return num1 + num2
#
#
# result = sum(10, 26)
# print(result)
#
#
# def sum(a, b):
#     num1 = a
#     num2 = b
#     return num1 - num2
#
#
# result = sum(10, 26)
# print(result)
#
#
# def sum(a, b):
#     num1 = a
#     num2 = b
#     return num1 * num2
#
#
# result = sum(10, 26)
# print(result)
#
#
# def sum(a, b):
#     num1 = a
#     num2 = b
#     return num1 / num2
#
#
# result = sum(10, 26)
# print(result)


# def fun(num):
#     print(num)
#     if num + 1 == 10:
#         return 10
#     return fun(num * (num + 1))
#
#
# result = fun(1)
# print(result)


# user_list = [{"Name": "isdigit", "QQ": 9527, "phone": 10086}]


# def test1():
#     while True:
#         name = str(input("请输入您的姓名："))
#         QQ = int(input("请输入您的QQ："))
#         phone = int(input("请输入您的手机号码："))
#         user_dict = {"Name": name, "QQ": QQ, "Phone": phone}
#         user_list.append(user_dict)
#         user_list[0][0] = name
#         user_list[0][1] = QQ
#         user_list[0][2] = phone
#         print(user_list)
#
#
# test1()
#
#
# name = "enumerate"
#
#
# def test1():
#     while True:
#         name = str(input("请输入您的姓名："))
#         QQ = int(input("请输入您的QQ："))
#         phone = int(input("请输入您的手机号码："))
#         user_dict = {"Name": name, "QQ": QQ, "Phone": phone}
#         # user_dict["Name"] = name
#         print(user_dict)
#
#
# test1()

# a = "1"
# b = "3"
#
#
# def test3(a="2", b="2"):
#     return a + b
#
#
# result = test3(a, b)
# print(result)

# list1 = ["isdigit", "randint", 1]
# list2 = ["import", "enumerate", 2]
#
#
# def test3(a, b):
#     list1 = [2, 6]
#     list2 = [5]
#     list1.append(a)
#     list2.append(b)
#     return len(list1) + len(list2)
#
#
# result = test3(list1, list2)
# print(result)


# def product(a, b):
#     return a + b


# def summer(num):
#     if 0 <= num <= 996:
#         result = num + summer(num - 1)
#     else:
#         result = False
#     return result
#
#
# while True:
#     n = input("请输入(0~996)的正整数(输入quit退出)：")
#     if n == "quit":
#         break
#     if n.isdigit() and 0 <= int(n) <= 996:
#         print(summer(int(n)))
#     else:
#         print("输入无效，已超出计算范围！")


# def summer(num):
#     if 0 <= num <= 996:
#         result = num - summer(num - 1)
#     else:
#         result = False
#     return result
#
#
# while True:
#     n = input("请输入(0~996)的正整数(输入quit退出)：")
#     if n == "quit":
#         break
#     if n.isdigit() and 0 <= int(n) <= 996:
#         print(summer(int(n)))
#     else:
#         print("输入无效，已超出计算范围！")


# def summer(num):
#     if 1 < num <= 996:
#         result = num / summer(num - 1)
#     elif num == 1:
#         result = 1
#     else:
#         result = False
#     return result
#
#
# while True:
#     n = input("请输入(1~996)的正整数(输入quit退出)：")
#     if n == "quit":
#         break
#     if n.isdigit() and 1 < int(n) <= 996:
#         print(summer(int(n)))
#     else:
#         print("输入无效，已超出计算范围！")


# def num(*args):
#     print(max(*args))
#     print(min(*args))
#
#
# num_list = []
# while True:
#     n = input("请输入数字(输入quit退出)：")
#     if n == "quit":
#         break
#     num_list.append(n)
# print(num_list)
# num(num_list)

# def fun(num):
#     if num >= 1:
#         result = num * fun(num - 1)
#     else:
#         result = 1
#     return result
#
#
# while True:
#     n = input("请输入一个正整数：")
#     if n == "quit":
#         break
#     print(f"{n}! = {fun(int(n))}")

# n = int(input("请输入一个正整数："))
# a = [i for i in range(1, n + 1)]
# b = [i for i in range(1, n + 1) if i % 2 == 0]
# c = [i for i in range(1, n + 1) if i not in b]
# print(b)
# print(c)

n = int(input("请输入一个正整数："))
a = [i for i in range(2, n + 1) if (n + 1) % i == 0]
b = [i for i in range(2, n + 1) if i not in a]
print(a)
# b = [j for j in range(1, i - 1) for ]


# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             break
#     else:
#         return True
#     return False
#
#
# print(is_prime(10))

# product(lambda a, b: a + b, lambda a, b: a ** b)

# summer = [i + for i in range(1, 6)]
# print(summer)
# value = [i for i in range(1, 6)]
# print(value)
# product = [i for i in range(1, 6)]
# print(value)
# consult = [i for i in range(1, 6) if i != 0]
#
# for i in range(1, 6):
#     result = i + 1
#     print(result)


# def factorial(num):
#     if num >= 1:
#         result = num * factorial(num - 1)
#     else:
#         result = 1
#     return result
#
#
# while True:
#     n = input("请输入您要求的阶乘(整数)(输入quit退出):")
#     if n == "quit":
#         break
#     if n.isdigit() and int(n) > 0:
#         print(factorial(n))
#     else:
#         print("输入无效，请重新输入大于0的整数！")


# 定义函数findall，实现对字符串find方法的进一步封装，要求返回符合要求的所有位置的起始下标，如字符串
# "helloworldhellopythonhelloc++hellojava"，需要找出里面所有的"hello"的位置，最后将返回一个元组(0,10,21,29)，
# 即将h的下标全部返回出来，而find方法只能返回第一个

# def findall():
# list = []
# str1 = "helloworldhellopythonhelloc++hellojava"
# str1.replace("hello", " ")
# print(str1)
# list.append(str1)
# for index, value in enumerate(str1):
    # str1.replace("hello")
    # print(str1.index("h"))
#     print(index)
#     print(value)
# print(list)

# a = [i for i in range(len(str1))]
# print(a)
# b = [str1[str1.index("h"): str1.index("h") + 5] for str1.index("h") in range(len(str1))]