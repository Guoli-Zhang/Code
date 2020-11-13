class GrandMather(object):
    def __init__(self):
        self.money = 10
        self.happy = "哈哈"

    def __str__(self):
        return f"我拥有{self.money},{self.happy}"


class GrandFather(object):
    def __init__(self):
        self.money = 100
        self.house = "海景别墅"

    def __str__(self):
        return f"我拥有{self.house}"


class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.happy = "哈哈哈"

    def job(self, time):
        self.money += time
        if 100 <= self.money <= 1000:
            self.happy = "哈哈哈"
        elif 1000 <= self.money < 10000:
            pass


class Mather(GrandMather, GrandFather):
    def work(self, time):
        self.money += time
        if 10 <= self.money <= 100:
            self.happy = "哈哈"
        elif 100 <= self.money < 1000:
            self.happy = "哈哈哈哈"


class Son(Mather, Father):
    def play(self):
        print("开火车")


son1 = Son()
son1.work(250)
son1.work(900)
son1.job(5000)
son1.job(4000)
son1.play()
print(son1)

