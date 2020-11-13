import os

os.chdir("../../../../../HelloWorld/python  NO.7/filter/")
title = "[黑马出品]"
while True:
    num = input("请输入执行命令（1.修改）（2.还原）：")
    if num == "quit":
        break
    files = os.listdir()
    if num == "1":
        if title in files[0]:
            print("已修改！")
        else:
            for i in files:
                os.rename(f"{i}", f"{title}{i}")
    elif num == "2":
        if title in files[0]:
            for i in files:
                os.rename(f"{i}", f"{i[len(title):]}")
        else:
            print("已还原")



# import os
#
# os.chdir("filter/")
# files = os.listdir()
# title = "tup"
# while True:
#     num = input("命令：")
#     if num == "quit":
#         break
#     if num == "1":
#         if title in files[0]:
#             print("已修改！")
#         else:
#             for i in files:
#                 os.rename(f"{i}", f"{title}{i}")
#     elif num == "2":
#         if title in files[0]:
#             for i in files:
#                 os.rename(f"{i}", f"{i[len(title):]}")
#         else:
#             print("已还原")
