# encoding=utf-8
# class People:
#     def __init__(self, name):
#         self.name = name
#
#
# people = People("name")
# people.name = "world"
# print(people.name)
#
#
# class People:
#     def __init__(self):
#         self.__name = "name"
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#
# people = People()
# print(people.get_name())
# people.set_name("十方")
#
#
# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     @staticmethod
#     def run():
#         print("run")
#
#
# class BMW(Car):
#     pass
#
#
# bmw = BMW("BMW", "red")
# print(bmw.name)
# print(bmw.color)
# bmw.run()


# def fun():
#     for col in range(1, 10):
#         for row in range(1, col + 1):
#             print(f"{row} × {col} = {col * row}\t", end=" ")
#         print("\n")
#
#
# fun()
# def findall(string, keyword):
#     str_list = []
#     for i in range(string.count(keyword)):
#         if i == 0:
#             str_list.append(string.find(keyword))
#         else:
#             str_list.append(string.find(keyword, str_list[i - 1] + 1))
#     return tuple(str_list)
#
#
# result = findall("helloworldhellopythonhelloc++hellojava", "hello")
# print(result)


# def findall(string, keyword):
#     str_list = []
#     for i in range(string.count(keyword)):
#         if i == 0:
#             str_list.append(string.find(keyword))
#         else:
#             str_list.append(string.find(keyword, str_list[i - 1] + 1))
#     return tuple(str_list)
#
#
# result = findall("helloworldhellopythonhelloc++hellojava", "hello")
# print(result)

# def findall(string, keyword):
#     str_list = []
#     for i in range(string.count(keyword)):
#         str_list.append(string.find(keyword)) if i == 0 else str_list.append(string.find(keyword, str_list[i - 1] + 1))
#     return tuple(str_list)
#
#
# result = findall("helloworldellopythonelloc++ellojava", "hello")
# print(result)


# import random
# ball = [["红", "红", "红", "红"], ["蓝", "蓝", "蓝", "蓝"], ["白", "白", "白", "白", "白"]]
# box = [[], [], []]
# for value in box:
#     ball_white = ball[2]
#     value.append(ball_white[len(ball_white) - 1])
#     ball_white.remove(value[0])
# for i in ball:
#     for j in i:
#         box[random.randint(0, 2)].append(j)
# print(box)

# import random
# # 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
# schools = [[], [], []]  # 办公室
# teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]  # 8位老师
# for value in schools:
#     value.append(teachers[len(teachers) - 1])
#     teachers.remove(value[0])
# for i in teachers:
#     schools[random.randint(0, 2)].append(i)
# print(schools)


# def fun(n):
#     list1 = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             list1.append(1)
#         else:
#             list1.append(list1[i - 2] + list1[i - 1])
#     print(list1)
#
#
# fun(20)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

# def fun(n):
#     list1 = []
#     for i in range(n):
#         list1.append(1) if i < 2 else list1.append(list1[i - 2] + list1[i - 1])
#     print(list1)
#
#
# fun(20)


# print(23 % 5)
# print(9 % 2)
# for i in range(0, 100):
#     if i % 10 != 3 and i // 10 != 3 and i % 3 != 0:
#         print(i)

# a = [i for i in range(0, 100) if i % 10 != 3 and i // 10 != 3 and i % 3 != 0]
# print(a)

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(9):
#     print(" " * (4 - i) + "*" * (2 * i + 1)) if i < 5 else print(" " * (i - 4) + "*" * (2 * (9 - i) - 1))
# if i < 5:
#     print(" " * (4 - i) + "*" * (2 * i + 1))
# else:
#     print(" " * (i - 4) + "*" * (2 * (9 - i) - 1))


# coding=utf-8
# loginUser = False
# user_list = [{"name":"系统管理员", "username":"admin", "passwd": "123456"}]
# while True:
#     print("      python攻城狮系统V6.0")
#     if not loginUser:
#         print("1.登录")
#     else:
#         print("1.登出")
#     print("2.注册新用户")
#     print("3.查看所有已注册用户")
#     print("4.管理员身份")
#     print("5.查看当前登录用户")
#     print("6.退出系统")
#
#     cmd = input("命令：")
#     # 登录登出管理
#     if cmd == "1":
#         # 如果是以登录状态，则询问是否注销登录
#         if loginUser:
#             yn = input("确认注销登录(y/n)")
#             if yn == "y":
#                 print("%s注销登录成功"%loginUser["name"])
#                 loginUser = False
#                 continue
#
#         # 如果是为登录状态，则进行登录
#         else:
#             username = input("请输入用户名：")
#             passwd = input("请输入密码：")
#             login = None    # 判断输入的用户是否存在
#             for user in user_list:
#                 # 判断输入的用户是否存在，以及密码是否正确
#                 if user["username"]==username and user["passwd"]==passwd:
#                     login = user
#             # 如果存在，且密码校验成功，则提示登录成功，并赋值非loginUser
#             # 否则提示"用户名密码错误或用户名不存在"
#             if login:
#                 print("欢迎%s，登录成功"%login["name"])
#                 loginUser = login
#             else:
#                 print("用户名密码错误或用户名不存在")
#     # 注册新用户，添加新用户
#     elif cmd == "2":
#         name = input("请输入昵称：")    # 昵称
#         username = input("请输入用户名(登录用):")    # 用户名，应判断是否存在
#         for user in user_list:
#             # 判断用户名是否因存在
#             if user["name"] == username:
#                 print("用户名%s已经存在，请重试")
#                 continue    # 如果存在，则重新输入
#         passwd1 = input("请输入密码：")
#         passwd2 = input("请确认密码：")
#         # 判断两次密码是否一致
#         if passwd1 != passwd2:
#             print("密码不一致，请重新输入")
#             continue    # 不一致则重新输入
#         # 否则，注册成功
#         newuser={"name":name, "username": username, "passwd":passwd1}
#         # 添加到用户列表
#         user_list.append(newuser)
#         print("注册成功")
#     # 查看所以已注册用户的信息，应具备管理员权限
#     elif cmd == "3":
#         # 判断是否已经登录
#         if loginUser:
#             # 判断当前用户是不是管理员
#             if loginUser["username"] != "admin":
#                 print("权限不足，请获取管理员权限")
#                 continue
#             else:
#                 i = 1
#                 for u in user_list:
#                     print("No%d. "%i, u)
#                     i += 1
#         else:
#             print("请以管理员身份登录并查看")
#
#     # 管理管理员账户
#     elif cmd == "4":
#         # 要求先登录
#         if not loginUser:
#             print("请先登录")
#             continue
#         else:
#             # 如果不是管理员
#             if loginUser["username"] != "admin":
#                 print("权限不足，请获取管理员权限")
#                 continue
#
#         for u in user_list:
#             if u["username"] == "admin" and loginUser["username"] == "admin":
#                 yn = input("需要修改管理员密码吗？(y/n)")
#                 if yn == "y":
#                     oldpasswd = input("请输入原密码：")
#                     if oldpasswd == loginUser["passwd"]:
#                         newpasswd = input("请输入新密码：")
#                         loginUser["passwd"] = newpasswd
#                         print("管理员密码已更新")
#                     else:
#                         print("密码错误，请重新输入")
#                         continue
#     # 查看当期那登录用户是谁
#     elif cmd == "5":
#         if loginUser:
#             print("当前登录的用户为%s(%s)"%(loginUser["name"], loginUser["username"]))
#         else:
#             print("当前登录的用户为匿名用户")
#     # 退出
#     elif cmd  == "6":
#         print("退出成功，谢谢您的使用！")
#         break


# print("123", end=" ")
# print("321")

# str1 = "qwertyuioplkjhgfdsa"
# print(str1[:-2])
# print(str1[-2:])
# print(str1[:4] + str1[8:])

# def fun1(*args, a, b, **kwargs):
#     print(args)
#     print(a)
#     print(b)
#     print(kwargs)
#
#
# fun1(5, 10, a=7, b=8, c="cc", d="dd")


# fun1 = lambda a, b: a - b
# result = fun1(2, 4)
# print(result)

# set1={4,5,2,1,3,9,8,1,2,3,5,6,7,8}
# print(set1)


# def product(part1, part2):
#     a = 1
#     b = 2
#     a = part1(a, b)
#     b = part2(a, b)
#     result = a ** b
#     print(result)
#
#
# product(lambda a, b: a + b, lambda a, b: a % b)

# a = [i for i in range(1, 101) if i // 10 != 7 and i % 10 != 7 and i % 7 != 0]
# print(a)
# b = [a[x:x + 3] for x in range(0, 100, 3)]
# print(b)

# for x in range(0, 100, 3):
#     print(x)

# names = ["apple", "enumerate", "index", "value", "return"]
# def f(x):
#     return x[0].upper() + x[1:]
#
# result = list(map(f, names))
# print(result)
#
# with open("a.txt", "w") as w:
#         w.write("Hello World")
# with open("a.txt", "a") as w:
#     w.write("Good")
# with open("a.txt", "w+") as w:
#     w.write("hh")
#     content = w.read()
#     print(content)
# with open("a.txt", "r+") as w:
#     w.write("cook")
#     content = w.read()
# with open("a.txt", "a+") as w:
#     w.write("Google")
#     content = w.read()
#     print(content)
# with open("a.txt", "r") as r:
#     content = r.read()
#     print(content)
#
# with open("a.txt", "r") as r:
#     content = r.read(10)
#     print(content)
#
# with open("a.txt", "r") as r:
#     content = r.readlines()
#     for i in content:
#         print(i, end="")
#
# with open("a.txt", "r") as r:
#     while True:
#         content = r.readline()
#         if content == " ":
#             break
#         print(content, end="")
# import os
# os.rename("a.txt", "b.txt")
# os.remove("b.txt")
# print(os.getcwd())
# os.mkdir("world")
# print(os.listdir())
# os.rmdir("world")

# while True:
#     file_name = input("请输入你要备份的文件名：")
#     if file_name == "quit":
#         break
#     new_name = file_name[:file_name.rfind(".")] + "-副本" + file_name[file_name.rfind("."):]
#     with open(file_name, "r") as r:
#         content = r.read()
#     with open(new_name, "w") as w:
#         w.write(content)

# import os
# while True:
#     num = input("请输入命令:")
#     if num == "quit":
#         break
#     files = os.listdir()
#     title = "fgg"
#     if num == "1":
#         if title in files[0]:
#             print("已改")
#         else:
#             for i in files:
#                 os.rename(f"{i}", f"{title}{i}")
#     elif num == "2":
#         if title in files[0]:
#             for i in files:
#                 os.rename(f"{i}", f"{i[len(title):]}")
#         else:
#             print("已复原！")










