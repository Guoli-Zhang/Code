class SweetPotato:
    def __init__(self, name):
        self.name = name
        self.state = "生的"
        self.total = 0

    def cook(self, time):
        self.total += time
        if 0 <= self.total < 3:
            self.state = "生的"
        elif 3 <= self.total < 6:
            self.state = "半生不熟"
        elif 6 <= self.total < 8:
            self.state = "熟了"
        elif self.total > 8:
            self.state = "糊了"

    def __str__(self):
        return f"{self.name}烤了{self.total}分钟，已经{self.state}"


SweetPotato1 = SweetPotato("大番薯")
SweetPotato1.cook(4)
SweetPotato1.cook(2)
print(SweetPotato1)
