class Dog:
    name = "旺财"

    def __init__(self):
        self.name = "来福"

    @staticmethod
    def eat():
        print("牛来福在吃东西")  # 无法调用类属性

    @staticmethod
    def eat():
        print("牛来福在吃旺财！")

    @classmethod
    def eat(cls):
        print(f"{cls.name}在吃东西")


dog1 = Dog
print(dog1.name)
dog1.eat()

dog1 = Dog()
print(dog1.name)
dog1.eat()
