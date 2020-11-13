student_list = []


def welcome_student():
    print("-" * 60)
    print()
    print("\t\t\t\t\t\t学生管理系统 V1.0")
    print()
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示所有学生")
    print("6:退出系统")
    print()
    print("-" * 60)


def empty_student():
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加!")
        return "1"


def check_name(name):
    for i in student_list:
        if name == i['name']:
            print("亲，学生管理系统里有人和您重名，这边建议您在名字后面加一个数字")
            break
    else:
        return "1"


def add_student():
    while True:
        name = input("请输入您的名字(输入quit代表返回学生管理系统界面)：")
        if name == "quit":
            return
        if check_name(name) == "1":
            break
    QQ = input("请输入您的QQ账号：")
    phone = input("请输入您的电话号码：")
    student_dict = {"name": name, "QQ": QQ, "phone": phone}
    student_list.append(student_dict)
    print(student_list)
    print(f"{name}的名片打印成功！")


def remove_student():
    if empty_student() == "1":
        return
    remove_num = input("请输入您要删除的学生序号：")
    if remove_num.isdigit():
        if 1 <= int(remove_num) <= len(student_list):
            remove_ok = input(f"你确定要把{student_list[int(remove_num) - 1]['name']}删除吗？(yes or no):")
            if remove_ok == "yes":
                print(f"{student_list[int(remove_num) - 1]['name']}删除成功！")
                student_list.pop(int(remove_num) - 1)
            else:
                print("您已经取消删除！")
        else:
            print("亲，序号超出范围，请正确输入！")
    else:
        print("请您正确输入数字序号！")


def modification_student():
    if len(student_list) == 0:
        print("亲，暂时没有任何数据，这边建议您先添加!")
        return
    modification_num = input("请输入您要修改的序号:")
    if modification_num.isdigit():
        if 1 <= int(modification_num) <= len(student_list):
            print("您要修改的学生信息是：")
            print(f"姓名：{student_list[int(modification_num) - 1]['name']}; "
                  f"{student_list[int(modification_num) - 1]['QQ']}; "
                  f"{student_list[int(modification_num) - 1]['phone']}")
            while True:
                new_name = input("请输入您的新名字(输入回车代表不修改名字)：")
                if new_name == "":
                    new_name = student_list[int(modification_num) - 1]['name']
                    break
                if check_name(new_name) == "1":
                    break
            new_QQ = input("请输入您的新QQ账号：")
            new_phone = input("请输入您的新电话号码：")
            if new_name == student_list[int(modification_num) - 1]['name']:
                modification_ok = input(f"您确定要修改{student_list[int(modification_num) - 1]['name']}的信息吗？"
                                        f"(yes or no):")
                if modification_ok == "yes":
                    print(f"{new_name}的信息修改成功！")
                    student_list[int(modification_num) - 1]['name'] = new_name
                    student_list[int(modification_num) - 1]['QQ'] = new_QQ
                    student_list[int(modification_num) - 1]['phone'] = new_phone
                else:
                    print("您已经取消修改！")
            else:
                modification_ok = input(f"您确定要把{student_list[int(modification_num) - 1]['name']}修改为"
                                        f"{new_name}吗？(yes or no):")
                if modification_ok == "yes":
                    print(f"{student_list[int(modification_num) - 1]['name']}修改为{new_name}成功！")
                    student_list[int(modification_num) - 1]['name'] = new_name
                    student_list[int(modification_num) - 1]['QQ'] = new_QQ
                    student_list[int(modification_num) - 1]['phone'] = new_phone
                else:
                    print("您已经取消修改！")
        else:
            print("亲，序号超出范围，请正确输入！")
    else:
        print("请您正确输入数字序号！")


def search_student():
    if empty_student() == "1":
        return
    search_name = input("请输入您要查询的名字：")
    for i in student_list:
        if search_name == i['name']:
            print(f"姓名：{search_name}\t\t\t\tQQ:{i['QQ']}\t\t\t\t手机：{i['phone']}")
            break
    else:
        print("查无此人！")


def show_student():
    if empty_student == "1":
        return
    print("序号\t\t\t\t姓名\t\t\t\tQQ\t\t\t\t手机")
    print("-" * 60)
    for index, value in enumerate(student_list):
        print(f"{index + 1}\t\t\t\t\t{value['name']}\t\t\t\t\t{value['QQ']}\t\t\t\t{value['phone']}")
    print()


def operation_student():
    num = input("请输入您的操作指令(数字)：")
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
        print("欢迎您再次使用学生管理系统")
        return False
    else:
        print("请根据操作指令前的数字正确输入您所需要的操作需求！")


while True:
    welcome_student()
    if operation_student() == False:
        break
