class GrandFather:
    def __init__(self):
        self.name = "祖父"
        self.height = 168

    def eat(self):
        print(f"{self.name}在吃东西")

    def show_height(self):
        print(f"{self.name}身高{self.height}cm")


class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.name = "父亲"


class Son(Father):
    def __init__(self):
        super(Father, self).__init__()

    def eat(self):
        super().eat()
        print("子类在吃东西")


# father = Father()
# father.eat()
# father.show_height()

son = Son()
son.eat()
son.show_height()