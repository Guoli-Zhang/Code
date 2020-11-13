# try:
#     print(10)
#
# except:
#     print("报错！")
#
#
# try:
#     print(name)
# except NameError:
#     print("此名不存在！")
#
# try:
#     print(10 + "11")
# except TypeError:  # 需判断错误类型
#     print("类型错误！")
#
# try:
#     print(10 + name)
# except Exception as e:
#     print(e)


class Dog:
    try:
        def __init__(self):
            name = "来福"
    except Exception as e:
        print(e)






