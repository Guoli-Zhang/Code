class Dog:
    def __init__(self, part1, part2, part3):
        self.name = part1
        self.colors = part2
        self.types = part3

    def __str__(self):
        return f"它的名字叫{self.name}"


dog1 = Dog()
print(dog1)


class Dog:
    def __del__(self):
        print("Oh, my god!")


dog2 = Dog()
# print(dog2)
