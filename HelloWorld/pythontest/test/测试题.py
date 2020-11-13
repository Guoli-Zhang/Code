# 一、单选题
# 1，A
# 2，B
# 3, B
# 4, B
# 5, D

# 二、判断题
# 1，Fasle
# 2, False
# 3, False
# 4, False
# 5, True
# 6, True
# 7, False
# 8, False
# 9, True
# 10, False

# 三、填空题
# 1， 无序
# 2， 9
# 3， [1, 2, 3, 4, 3]
# 4, (3,) ； 3
# 5， 形参 ； 实参
# 6， 列表、元组、字典
# 7， id()
# 8, 字符串、列表、字典、集合 ; 元组
# 10, 缺省

# 四、代码题
# 1， 如下：

# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%2d * %2d = %2d" %(i, j, i * j), end = " ")
#         j += 1
#     print()
#     i += 1


# 2, 如下：

# dict1 = {"1":"!", "2":"@", "3":"#", "4":"$", "5":"%", "6":"^", "7":"&","8":"*", "9":"(", "0":")"}
# while True:
#     user = input("请输入您要查询的数字(按q退出）：")
#     if user == "q":
#         break
#     if len(user) == 1 and user.isdigit():
#         print(dict1[user])
#     else:
#         print("未收录该字符的含义，请重新输入")


# 3, 如下：

def fun(s, a1, a2):
    return s.replace(s[a1:a2 + 1], "")
s = input("请输入您要操作的字符串：")
while True:
    a1 = input("请输入切割起始位置(数字)：")
    if a1.isdigit():
        a1 = int(a1)
        if a1 < len(s):
            break
        else:
            print("超过范围，请重新输入")
    else:
        print("请输入数字")
while True:
    a2 = input("请输入切割结束位置(数字):")
    if a2.isdigit():
        a2 = int(a1)
        if a2 < len(s):
            break
        else:
            print("超过范围，请重新输入")
    else:
        print("请输入数字")

print(fun(s, a1, a2))