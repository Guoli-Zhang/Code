class Dog:
    def __init__(self, part1, part2, part3):
        self.types = part1
        self.names = part2
        self.colors = part3

    def show_types(self):
        print(f"这是一只{self.colors}叫{self.names}的{self.types}")


dog1 = Dog("小狗", "旺财", "黑色")
dog1.show_types()

dog2 = Dog("中狗", "小黄", "白色")
dog2.show_types()

dog3 = Dog("大狗", "小花", "黑白相间")
dog3.show_types()
