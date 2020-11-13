# encoding=utf-8


def star_student():
    student_manager = StudentManager()
    student_manager.deal_student()


class Student:
    def __init__(self, name, qq, phone):
        self.name = name
        self.qq = qq
        self.phone = phone

    def information(self):
        return {"name": self.name, "qq": self.qq, "phone": self.phone}


class StudentManager:
    def __init__(self):
        self.student_list = []

    @staticmethod
    def welcome_student():
        print("-" * 80)
        print()
        print("\t\t\t\t\t学生管理系统 V1.0")
        print()
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生")
        print("4.查询学生")
        print("5.显示所有学生")
        print("6.保存学生文档")
        print("7.退出学生管理系统")
        print()

    def add_student(self):
        name = input("请输入姓名：").strip()


    def deal_student(self):
        while True:
            self.welcome_student()
            num = input("请输入操作指令(数字)：")
            if num == "1":
                print("您选择的操作是：添加学生")
            elif num == "2":
                print("您选择的操作是：删除学生")
            elif num == "3":
                print("您选择的操作是：修改学生")
            elif num == "4":
                print("您选择的操作是：查询学生")
            elif num == "5":
                print("您选择的操作是：显示所有学生")
            elif num == "6":
                print("您选择的操作是：保存学生文档")
            elif num == "7":
                print("欢迎再次使用学生管理系统")
                return
            else:
                print("请您正确输入！")





