#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# print(" " * 4 + "*" * 1)
# print(" " * 3 + "*" * 3)
# print(" " * 2 + "*" * 5)
# print(" " * 1 + "*" * 7)
# print(" " * 0 + "*" * 9)
# print(" " * 1 + "*" * 7)
# print(" " * 2 + "*" * 5)
# print(" " * 3 + "*" * 3)
# print(" " * 4 + "*" * 1)

# i = 1
# j = 4
# k = 7
# g = 1
# while i < 10 and j >= 0:
#     print(" " * j + "*" * i)
#     i += 2
#     j -= 1
# while k > 0 and g < 5:
#     print(" " * g + "*" * k)
#     k -= 2
#     g += 1

# i = 1
# j = 4
# k = 11
# g = 0
# while i < 10 and j >= 0:
#     print(" " * j + "*" * i)
#     i += 2
#     j -= 1
#     if i >= k and j <= g:
#         i -= 4
#         k -= 4
#         j += 2
#         g += 2
#         if i == -1 and j == 5:
#             break

# age = 18
# if age > 18:
#     print("您已成年！")
# elif age == 18:
#     print("您刚好成年！")
# else:
#     print("您未成年！")

# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("允许上网！")
# else:
#     print("禁止入内！")

# car = int(input("请问您有几辆车："))
# house = int(input("请问您有几套房："))
# love = bool(input("请问您是否爱我的女儿："))
# if car >= 3 and house >= 2 and love == True:
#     print("能结婚！")
# else:
#     print("不能结婚！")

# car = int(input("请问您有几辆车："))
# house = int(input("请问您有几套房："))
# love = bool(input("请问您是否爱我的女儿："))
# if car >= 3 or house >= 2 or love == True:
#     print("能结婚！")
# else:
#     print("不能结婚！")

# love = bool(input("请问您是否爱我的女儿："))
# if not love == True:
#     print("能结婚！")
# else:
#     print("不能结婚！")

# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("允许上网！")
# elif age >= 17:
#     print("过两天再来上网！")
# elif age >= 12:
#     print("存两年钱在来上网！")
# else:
#     print("小屁孩还敢来网吧，一会告诉你妈去！")

# 使用 while 循环计算5!
# i = 1
# result = 1
# while i <= 5:
#     result = result * i
#     i += 1
# print(result)

# i = 1
# result = 1
# while i <= num:
#     result = result * i
#     i += 1
# print(result)

# num = 10
# i = 0
# result = 0
# while i <= num:
#     result = result + i
#     if result == 5:
#         break
#     i += 1

# i = 0
# while True:
#     i += 1
#     if i == 5:
#         break
# print("刷碗数为：%d" % i)

# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

# date = int(input("请输入日期："))
# if date <= 7 and date == 6 or date == 7:
#     print("周末")
# elif date < 6 and date == 1:
#     print("周一")
# elif date < 6 and date == 2:
#     print("周二")
# elif date < 6 and date == 3:
#     print("周三")
# elif date < 6 and date == 4:
#     print("周四")
# elif date < 6 and date == 5:
#     print("周五")

# date = int(input("请输入日期："))
# if date <= 7 and date == 6 or date == 7:
#     print("周末")
# else:
#     print("工作日")

# date = int(input("请输入日期："))
# if date <= 7 and date == 6 or date == 7:
#     print("周末")
# elif 5 >= date >= 1:
#     print("工作日")
# else:
#     print("错误")

# height = float(input("请输入您的身高："))
# weight = float(input("请输入您的体重："))
# BMI = float(weight / (height * height))
# print("BMI = %.2f" % BMI)
# if BMI < 18.5:
#     print("您的体重过轻！")
# elif 25 > BMI >= 18.5:
#     print("您的体重正常！")
# elif 28 > BMI >= 25:
#     print("您的体重过重！")
# elif 32 > BMI >= 28:
#     print("您的体重偏肥胖！")
# elif BMI > 32:
#     print("您的体重属于严重肥胖，请注意均衡饮食，多运动！")

# import random
#
# player = int(input("请输入您要出的拳，剪刀（0）/石头（1）/布（2）:"))
# computer = random.randint(0, 2)
# print("电脑出的拳是：%d" % computer)
# if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print("玩家胜利！")
# elif player == computer:
#     print("平局")
# else:
#     print("电脑胜利！")
# if computer == 0:
#     str1 = "剪刀"

# 编写一个程序计算个人所得税（以下为个人所得税税率表，3500元起征）：
# 应纳税所得额(含税)                        税率(%)
# 不超过1500元的                              3        45     5000
# 超过1500元至4,500元的部分                   10       345     8000
# 超过4,500元至9,000元的部分                  20       1245    12500
# 超过9,000元至35,000元的部分                 25       7745    38500
# 超过35,000元至55,000元的部分                30       13745   58500
# 超过55,000元至80,000元的部分                35       38745   83500
# 超过80,000元的部分                          45
# income = float(input("请输入您的收入："))
# if 5000 >= income >= 3500:
#     tax1 = (income - 3500) * 0.03
#     print("您应缴纳的个人所得税为：%.2f" % tax1)
# elif 8000 >= income > 5000:
#     tax2 = 45 +(income - 5000) * 0.10
#     print("您应缴纳的个人所得税为：%.2f" % tax2)
# elif 12500 >= income > 8000:
#     tax3 = 345 + (income - 8000) * 0.20
#     print("您应缴纳的个人所得税为：%.2f" % tax3)
# elif 38500 >= income > 12500:
#     tax4 = 1245 + (income - 12500) * 0.25
#     print("您应缴纳的个人所得税为：%.2f" % tax4)
# elif 58500 >= income > 38500:
#     tax5 = 7745 + (income - 38500) * 0.30
#     print("您应缴纳的个人所得税为：%.2f" % tax5)
# elif 83500 >= income > 58500:
#     tax6 = 13745 + (income - 58500) * 0.35
#     print("您应缴纳的个人所得税为：%.2f" % tax6)
# elif income > 83500:
#     tax7 = 38745 + (income - 83500) * 0.45
#     print("您应缴纳的个人所得税为：%.2f" % tax7)
# else:
#     print("您不需要缴纳个人所得税")

#     print("电脑输出的拳是：%s" % str1)
# elif computer == 1:
#     str2 = "石头"
#     print("电脑输出的拳是：%s" % str2)
# elif computer == 2:
#     str3 = "布"
#     print("电脑输出的拳是：%s" % str3)
#     if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#         print("玩家胜利！")
#     elif player == computer:
#         print("平局")
#     else:
#         print("电脑胜利！")

# 编写代码设计简易计算器，可以进行基本的加减乘除运算。
#
# 用户输入第一个数字
# 用户输入一个操作符 +、-、*、/
# 用户输入第二个数字
# 判断运算类型，并进行计算

# num1 = float(input("请您输入第一个数字："))
# str = input("请您输入第一个操作符：(+)，(-)，(*)，(/):")
# num2 = float(input("请您输入第二个数字："))
# if str == "+":
#     result = num1 + num2
#     print("您的数据输入得到的结果是：%.2f" % result)
# elif str == "-":
#     result = num1 - num2
#     print("您的数据输入得到的结果是：%.2f" % result)
# elif str == "*":
#     result = num1 * num2
#     print("您的数据输入得到的结果是：%.2f" % result)
# elif str == "/":
#     result = num1 / num2
#     print("您的数据输入得到的结果是：%.2f" % result)
# else:
#     print("无效命令")

# *
# * *
# * * *
# * * * *
# * * * * *

# i = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# * * * * *
# * * * *
# * * *
# * *
# *
# i = 5
# while i >= 0:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i = i-1

# i = 5
# while i >= 0:
#     print("*" * i)
#     i = i-1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         if j == 4:
#             break
#         print(1 * j)
#         j += 1
#     print(1 * i)
#     i += 1

# i = 1
# j = 1
# num = None
# while i < 10:
#     result = 1 * i
#     print("1×=%d" % result)
#     # j = 1
#     # while j < 10:
#     #     print(j * j)
#     #     j += 1
#     # print(i * i)
#     i += 1

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# i = 1
# while i <= 5:
#     j = 4
#     while j > i:
#         print("*" * j)
#         j = j - 1
#     print("*" * i)
#     i += 1

# print(" * " * 1)
# print(" * " * 2)
# print(" * " * 3)
# print(" * " * 4)
# print(" * " * 5)
# print(" * " * 4)
# print(" * " * 3)
# print(" * " * 2)
# print(" * " * 1)

# print("*" * 1 + " " * 4)
# print("*" * 2 + " " * 3)
# print("*" * 3 + " " * 2)
# print("*" * 4 + " " * 1)
# print("*" * 5 + " " * 0)
# print("*" * 4 + " " * 1)
# print("*" * 3 + " " * 2)
# print("*" * 2 + " " * 3)
# print("*" * 1 + " " * 4)

# while True:
#     user = str(input("请在此处填写你的用户名："))
#     password = int(input("请在此处输入您的密码："))
#     if password != 123456:
#         break
#     elif user == "python" and password == 123456:
#         print("欢迎光临!")

# 使用while、if来完善剪刀石头布程序，要求，当一局猜拳结束能立即开始下一局猜拳。
# import random
#
# win = 0
# while True:
#     player = int(input("您出的拳是 剪刀（0）/石头（1）/布（2）:"))
#     computer = random.randint(0,2)
#     print("电脑输出的拳是：%d" % computer)
#     if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#         print("玩家胜利！")
#         win += 1
#         print("玩家胜利的次数是：%d" % win)
#         if win == 3:
#             break
#     elif player == computer:
#         print("平局！")
#     else:
#         print("电脑胜利！")


# i = 1
# while i <= 5:
#     print(" * " * i)
#     i += 1
# j = 4
# while j > 0 :
#     print(" * " * j)
#     j -= 1

# i = 1
# j = 6
# while i < 6:
#     print(" * " * i)
#     i += 1
#     if i >=j:
#         i -= 2
#         j -= 2
#         if i == 0:
#             break


# i = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# 设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字
i = 1
while i <= 100:
    if i % 7 == 0:
        i += 1
        continue
    print("%d" % i)
    i += 1


# print("Hello World!"*2)
#
# # print("Hello World!"*2)
#
# str1="hello"
# str2="python"
# print("str1+str2")
#
# a=1
# a=a+1
#
# price=6
# print("数值：.2f%" % price)
#
a=10
b=30
c=a*b
print("a为：%02d,b为:%02d,c为：%02d" % (a,b,c))

# name=input("请输入您的名字：")
# gender=input("请输入您的性别：")
# age=input("请输入您的年龄：")
# unit=input("请输入您的单位：")
# QQ=input("请输入您的QQ号码：")
# phone=("请输入您的联系电话：")
# address=input("请输入您的家庭住址：")
# print("="*10+"你的名片"+"="*10)
# print("姓名：%s" % name)
# print("性别：%s" % gender)
# print("年龄：%s" % age)
# print("单位：%s" % unit)
# print("QQ:%s" % QQ)
# print("phone:%s" % phone)
# print("住址：%s" % address )
# print("="*28)

price=3.2
weight=6.5
money=price*weight
print("苹果的单价为：%.2f元/斤，买了%.2f斤，您一共支付%.2f元"% (price,weight, money))

# str1 = '传智'
# str2 = "播客"
# str3 = """黑马"""
# str4 = '''Python'''

# str5 = "100"
# int1 = 100
#
# int2 = int(str5)
# print(int2)
#
# str6 = str(int1)
# print(str6)

# num1 = 1
# print(type(num1))

# 编程题：从键盘输入一个用户名和密码，判断是否正确，如果是则打印登录系统成功，否则显示用户名或密码错误
# user = str(input("请输入您的用户名："))
# password = int(input("请输入您的密码："))
# str1 = "孤筏重洋"
# int1 = 134679
# if user == str1 and password == int1:
#     print("登录系统成功")
# elif user != str1:
#     print("用户名错误")
# elif password != int1:
#     print("密码错误")

# 名片管理器v1.0，记录一张名片
# 使用个三个变量来记录用户输入的信息，包含姓名、电话、性别
# 打印名片信息，程序结束
# name = str(input("请输入您的姓名："))
# phone = int(input("请输入您的电话号码："))
# gender = str(input("请输入您的性别："))
# list1 = [
#     name,
#     phone,
#     gender
# ]
# print("-" * 10 + "您的名片" + "-" * 10)
# print("姓名：%s" % name)
# print("电话：%d" % phone)
# print("性别：%s" % gender)
# print("-" * 27)
# print(list1)
# print("-" * 10 + "您的名片" + "-" * 10)
# print(f"姓名:{name}, 电话：{phone}, 性别：{gender}")
# print("-" * 27)

# 编程, 使用[字典]来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自键盘的输入，所有数据添加到字典后打印字典变量。
# person = {"name": input("请输入您的姓名："), "age": input("请输入您的年龄："), "account": input("请输入您的学号："), "QQ": input("请输入您的QQ："),
#           "WeChat": input("请输入您的微信："), "address": input("请输入您的住址："), "Email": input("请输入您的邮箱：")}
# print(person)

# 完成字符串的长度统计以及逆序打印
#
# 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
# 打印出字符串长度
# 使用切片逆序打印出字符串
# user = [input("请输入用户名：")]
# if len(user[0]) > 31:
#     print("请重新输入")
# else:
#     print("欢迎注册！")
# print(user[0][::-1])

# 要求从键盘输入用户名和密码
# 校验格式是否符合规则，用户名长度6-20，并且用户名必须以字母开头
# 如果不符合，打印出不符合的原因，并再次提示输入
# user = [input("请输入用户名："), input("请输入密码：")]
# if len(user[0]) < 6 or 20 < len(user[0]) or False == str.isalpha(user[0][0]):
#     print("输入不规范，用户名第一位请输入字母，请再次输入！")

# 名片管理器v1.0 升级版，记录一张名片
#
# 使用个三个变量来记录用户输入的信息，包含姓名、电话、性别
# 姓名长度不是在6-20范围内，则提示错误
# 电话号码长度不是11，则提示错误
# 性别不是男或女，则提示错误
# 任意一样信息为空，则提示错误
# 所有信息校验通过后，打印名片信息，程序结束
person = [input("请输入姓名："), input("请输入电话："), input("请输入性别：")]
if len(person[0][0]) > 20 or len(person[0][0]) < 6 or len(person[1][0]) != 11 or person[2][0] != "男" or person[2][0] != "女":
    print("输入错误！")

# 编写一段代码，求1-100之间所有整数的和
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)

# result = 0
# for i in range(101):
#     result += i
# print(result)


# def fun1():
#     """1-100之间所有整数的和"""
#     result = 0
#     for i in range(1, 101):
#         result += i
#     print(result)
#
#
# fun1()


# result = 0
#
#
# def fun1(a, b):
#     fun1(1, 100)
#
#
# print(result)

# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字:"))
# result = 0
# for i in range(num1, num2):
#     result += i
# print(result)


# def fun1(a, b):
#     num1 = a
#     num2 = b
#     result = 0
#     for i in range(num1, num2):
#         result += i
#     return result
#
#
# result = fun1(1, 10)
# print(result)


# def test1():
#     print("test1")
#     print("这里是test1函数执行的代码")
#     print("test1")
#
#
# def test2():
#     print("这里是test2函数执行的代码")
#     test1()
#     print("test2")
#
#
# test2()
#
#
# def fun1(a, b):
#     num1 = a
#     num2 = b
#     print("I'm here")
#     return num1 ** num2
#
#
# def fun2(c, d):
#     num3 = c
#     num4 = d
#     print("look")
#     fun1(2, 6)
#     return num3 * num4
#
#
# print(fun1(2, 6))
# result2 = fun2(4, 6)
# print(result2)


# 写一个程序，由用户输入一个年份，用函数实现判断是否是闰年。
# 年份作为参数传递给函数
# 函数需要有返回值
#
# num1 = int(input("请输入年份："))
#
#
# def year(part1):
#     num1 = part1
#     if num1 // 4 == 0:
#         print("闰年")
#     return num1
#
#
# result = year(num1)
# print(result)


# str1 = "a, b, c, d"


# 需求：统计出以下文章中的字数，空格不算
# str1 = "“车岭车上    天，九岭爬    九年”。当年“三进下    党”的场景，我至今还历    历在目。经过30年的不懈奋斗，下党天" \
#        "    堑变通途、旧貌换    新颜，乡亲们有了越来越多   " "的幸福感、获得感，这生动印证了弱鸟先飞、滴水穿    石的道理。 "
# print(len(str1) - str1.count(" ") - str1.count("、") - str1.count("。") - str1.count("，") - str1.count("“") -
#       str1.count("”"))

# 需求：列表去重-把列表中相同的数据去掉;注意：删除大量列表中的数据，会删除不干净
# list1 = [1, 212, 3, 1, 2, 8, 9, 2, 3, 1, 2, 3, 4, 5, 5, 6, 8, 9, 9]
# num_list = []
# for i in list1:
#     if i not in num_list:
#         num_list.append(i)
# num_list.sort()
# print(num_list)

# 需求：把左右两边空格去掉。不能用lstrip，不能写死
# str1 = "      哈哈    呵呵      "
# str1 = str1.replace(" ", "")
# print(str1)

# while str1(0) = " ":
#     str1(1:)

# 需求：生成10个0-3的随机数的列表  例如：[0,1,1,2,3,3,2,1,2,1]
# import random
#
# num_list = []
# i = int(len(num_list))
# for i in range(10):
#     num_list.append(random.randint(0, 3))
# print(num_list)



