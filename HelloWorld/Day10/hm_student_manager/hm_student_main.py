# encoding=utf-8
class Student:
    """学生类"""
    def __init__(self, name, qq, phone):
        self.name = name
        self.qq = qq
        self.phone = phone

    def information(self):
        """学生提供的信息"""
        return {"name": self.name, "qq": self.qq, "phone": self.phone}


class StudentManager:
    """学生管理类"""
    def __init__(self):
        self.student_list = []  # 存放所有学生的信息
        self.load_student()

    @staticmethod
    def welcome():
        """欢迎界面"""
        print("-" * 70)
        print("学生管理系统 V1.0")
        print("")
        print("1:添加学生")
        print("2:删除学生")
        print("3:修改学生")
        print("4:查询学生")
        print("5:显示所有学生")
        print("6:退出系统")
        print("")
        print("-" * 70)

    def deal(self):
        """操作选项"""
        while True:
            self.welcome()

            num = input("请输入要进行的操作(数字)：")

            if num == "1":
                print("您选择的是：添加学生")
                self.add_student()
                self.save_student()
            elif num == "2":
                print("您选择的是：删除学生")
                self.remove_student()
                self.save_student()
            elif num == "3":
                print("您选择的是：修改学生")
                self.change_student()
                self.save_student()
            elif num == "4":
                print("您选择的是：查询学生")
                self.search_student()
            elif num == "5":
                print("您选择的是：显示所有学生")
                self.show_student()
            elif num == "6":
                print("欢迎再次使用~~~")
                break
            else:
                print("请正确输入操作序号")

    def check_name(self, name):
        """判断是否重名"""
        for names in self.student_list:
            if name == names["name"]:
                print("有人重名了")
                return "1"

    def add_student(self):
        """添加学生"""
        name = input("请输入姓名：")

        if self.check_name(name) == "1":
            return

        qq = input("请输入QQ：")
        phone = input("请输入手机：")

        student = Student(name, qq, phone)

        # 往列表中追加 此对象的方法。此对象的方法返回了学生的详细信息
        self.student_list.append(student.information())
        print(self.student_list)

    def check_list(self):
        """判断列表是否为空"""
        if len(self.student_list) == 0:
            print("暂时还没有学生，请先添加")
            return "1"

    def show_student(self):
        """显示学生"""
        if self.check_list() == "1":
            return

        print("序号\t\t\t\t姓名\t\t\t\tQQ\t\t\t\t手机号")
        print("-" * 70)

        for index, students in enumerate(self.student_list):
            print(f"{index + 1}\t\t\t\t{students['name']}\t\t\t\t{students['qq']}\t\t\t\t{students['phone']}")

    def search_student(self):
        """查询学生"""
        if self.check_list() == "1":
            return

        name = input("请输入您要查询的名字：")

        for names in self.student_list:
            if name == names['name']:
                print(f"姓名：{names['name']}；手机号：{names['phone']}；QQ：{names['qq']}；")
                break
        else:
            print("查无此人")

    def remove_student(self):
        """删除学生"""
        if self.check_list() == "1":
            return

        num = input("请输入您要删除的序号：")

        if num.isdigit():  # 判断是否数字的字符串
            num = int(num) - 1

            if 0 <= num < len(self.student_list):  # 判断序号是否在我们的范围内

                remove_ok = input(f"您确定要把 {self.student_list[num]['name']} 删掉吗？yes or no：")

                if remove_ok == "yes":
                    print(f"{self.student_list[num]['name']} 删除成功")
                    self.student_list.pop(num)
                else:
                    print("取消删除")
            else:
                print("您输入的序号，超出了范围")
        else:
            print("请输入数字序号")

    def change_student(self):
        """修改学生"""
        if self.check_list() == "1":
            return

        num = input("请输入您要修改的序号：")

        if num.isdigit():
            num = int(num) - 1
            if 0 <= num < len(self.student_list):
                sl = self.student_list[num]
                print(f"姓名：{sl['name']}；手机号：{sl['phone']}；QQ号：{sl['qq']}")

                while True:
                    new_name = input("请输入新的名字(不更改姓名，直接按回车)：").strip()
                    if new_name == "":
                        new_name = sl['name']
                        break

                    for names in self.student_list:
                        if new_name == names['name']:
                            print("名字重复了")
                            break
                    else:
                        break

                new_qq = input("请输入新的QQ：").strip()
                new_phone = input("请输入新的手机号：").strip()

                if new_name == sl['name']:
                    print(f"{new_name} 修改成功")
                else:
                    print(f"{sl['name']} 修改为 {new_name} 成功")

                sl['name'] = new_name
                sl['qq'] = new_qq
                sl['phone'] = new_phone

    def save_student(self):
        """保存信息"""
        with open("hm_student_info.hm", "w") as w:
            w.write(str(self.student_list))

    def load_student(self):
        """读取信息"""
        try:
            with open("hm_student_info.hm", "r") as r:
                content = r.read()
                self.student_list = eval(content)
        except:
            pass


def start():
    """把启动页面的代码放在这"""
    student_manager = StudentManager()
    student_manager.deal()
