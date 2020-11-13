student_list = []  # 全局变量
# welcome


def welcome():
    """welcome"""
    print("-" * 60)
    print()
    print("\t\t\t\t\t学生管理系统 V1.0")
    print()
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示所有学生")
    print("6:退出系统")
    print()
    print("-" * 60)


def add_student():
    """add_student"""
    while True:   # 如果姓名重复，需要重复询问添加
        name = input("请输入您的名字（输入quit代表返回学生管理系统界面）：")
        if name == "quit":
            return
        for i in student_list:   # 问完之后，立即判断是否有重名
            if name == i['name']:
                print("亲！学生管理系统里有人和你重名，这边建议你在名字后面加一个数字")
                break  # 重名，跳出for循环，执行while True循环,再问
        else:
            break   # 姓名不重复，跳出while True循环，执行下一命令
    QQ = input("请输入您的QQ账号：")
    phone = input("请输入你的电话号码：")
    address = input("请输入你的家庭住址：")
    # 创一个学生字典
    student_dict = {"name": name, "QQ": QQ, "phone": phone, "address": address}
    # 将学生字典添加到学生列表里（列表必须放在全局变量里）
    student_list.append(student_dict)
    print(student_list)  # 打印列表
    print(f"{name}的名片打印成功！")


def show_student():
    """show"""
    # 判断是否有学生
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加！")
        return
    print("序号\t\t\t\t姓名\t\t\t\tQQ\t\t\t\t手机\t\t\t\t住址")
    print("-" * 60)
    for index, value in enumerate(student_list):
        print(f"{index + 1}\t\t\t\t{value['name']}\t\t\t\t{value['QQ']}\t\t\t\t{value['phone']}\t\t\t\t{value['address']}")
    # for i in student_list:
    #     for j in i.values:
    #         print(j, "\t\t\t\t")
    #     print()


def search_student():
    """search"""
    # 先判断
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加！")
        return
    name = input("请输入您要查询的名字：")
    for i in student_list:
        if name == i['name']:
            print(f"姓名：{i['name']}\t\t\tQQ:{i['QQ']}\t\t\t电话号码:{i['phone']}\t\t\t住址：{i['address']}")
            break
    else:
        print("查无此人")


def remove_student():
    """remove"""
    # 先判断
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加！")
        return
    num = input("请输入您要删除的序号:")
    if num.isdigit():
        if 1 <= int(num) <= len(student_list):
            remove_ok = input(f"您确定要把{student_list[int(num) - 1]['name']}删除吗？(Y or N):")
            if remove_ok == "Y":
                print(f"{student_list[int(num) - 1]['name']}删除成功")
                student_list.pop(int(num) - 1)
            elif remove_ok == "N":
                print("已经取消删除！")
        else:
            print("亲，序号超出范围，请您正确输入！")
    else:
        print("请您正确输入数字序号！")


def modification_student():
    """modification"""
    # 先判断
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加！")
        return
    num = input("请输入您要修改的序号：")
    if num.isdigit():
        if 1 <= int(num) <= len(student_list):
            print("您要修改的学生信息是：")
            print(f"姓名：{student_list[int(num) - 1]['name']}; QQ:{student_list[int(num) - 1]['QQ']}; "
                  f"phone:{student_list[int(num) - 1]['phone']}; 住址：{student_list[int(num) - 1]['address']}；")
            new_name = input("请输入您的新名字：")
            if new_name == student_list[int(num) - 1]['name']:
                print("name+1")
            else:
                new_QQ = input("请输入您的新QQ账号：")
                new_phone = input("请输入您的新电话号码：")
                new_address = input("请输入您的新住址：")
                modification_ok = input(f"您确定要把xx修改为xx吗？(Y or N:)")
                if modification_ok == "Y":
                    print(f"{student_list[int(num) - 1]['name']}修改为{new_name}成功！")
                    student_list[int(num) - 1]['name'] = new_name
                    student_list[int(num) - 1]['QQ'] = new_QQ
                    student_list[int(num) - 1]['phone'] = new_phone
                    student_list[int(num) - 1]['address'] = new_address
                elif modification_ok == "N":
                    print("已经取消修改！")
        else:
            print("亲，序号超出范围，请你正确输入！")
    else:
        print("请您正确输入数字序号！")


def operation():
    """operation"""
    num = input("请您正确输入需要的操作（数字）：")
    if num == "1":
        print("您选择的操作是：添加学生")
        add_student()
    elif num == "2":
        print("您选择的操作是：删除学生")
        remove_student()
    elif num == "3":
        print("您选择的操作是：修改学生")
        modification_student()
    elif num == "4":
        print("您选择的操作是：查询学生")
        search_student()
    elif num == "5":
        print("您选择的操作是：显示所有学生")
        show_student()
    elif num == "6":
        print("欢迎您再次使用学生管理系统！")
        return False
    else:
        print("请您正确输入需要操作的数字序号！")


while True:
    welcome()

    if operation() == False:
        break

