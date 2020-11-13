# 要修改一个对象的属性有几种方法,分别是什么?
# 答：定义属性为形参，传实参修改; 在定义属性里修改。
# 保护属性的安全性的一般处理方式是什么?
# 答:转为私有属性。
# 要想将一个属性私有化,该怎么做?
#  答：self.__属性
# 在Python中属性有哪几种权限?
# 答：私有权限、公有权限
# 定义一个people类,其中要有类的初始化函数(带参数name).
# class People:
#     def __init__(self):
#         self.name = "name"
# people = People()
# print(people.name)
# 如何将上述的name改成私有属性?
# class People:
#     def __init__(self):
#         self.__name = "name"
# people = People()
# print(people.__name)
# 此时在类外还能访问到name吗?
#  不能
# 在类内可以访问到name吗?
# 能
# 如果想要在类外访问到name该怎么办?
# class People:
#     def __init__(self):
#         self.__name = "name"
#
#     def change_name(self):
#         self.name = "name"
#
#     def show_name(self):
#         print(self.__name)
# people = People()
# people.show_name()
# 在类内定义一个可以调用私有属性name的函数.
# class People:
#     def __init__(self):
#         self.__name = "name"
#
#     def change_name(self):
#         self.name = "name"
#
#     def show_name(self):
#         print(self.__name)
# people = People()
# people.show_name()
# 如果要想修改私有属性name该怎么办?
# class People:
#     def __init__(self):
#         self.__name = "name"
#
#     def change_name(self):
#         self.name = "name"
#
#     def show_name(self):
#         print(self.__name)
# people = People()
# people.show_name()
# 大家是如何理解单继承的?
# 一个子类继承父类
# 请写出单继承的格式?
# class GrandFather:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def house(self):
#         print("我有一所房子，面朝大海，春暖花开！")
# class Father(GrandFather):
#     pass
# father = Father("李海生", "40")
# father.house()
# 请写出一个Car基类,BMW类继承于Car类,基类中有init方法(包含name,color)和run方法.
# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def run(self):
#         print("风驰天下！")
#     def __str__(self):
#         return f"{self.color}的{self.name}在公路上奔腾！"
# class BMW(Car):
#     pass
# Bmw = BMW("BMW", "红色")
# print(Bmw)
# Bmw.run()
# 如果子类中没有定义init方法,但是要实例化一个对象,那此时会调用父类的构造方法吗?
# 会
# 如果子类重写了init方法,那么在实例化对象的时候,你觉得会调用哪个构造方法,是父类的还是子类的?
# 子类的
# 当子类重写init方法,在实例化对象的时候,如果想要调用父类的init方法该怎么办?
# super().__init__()
# 类中的私有属性能通过对象直接访问吗?
# 不能
# 要想访问类中的私有属性该怎么办?
# 在类中定义一个函数修改或者在类内部访问。
# 基类中的私有属性能被子类继承吗?
# 不能
# 那么私有属性存在的意义是什么?
# 私有
# 对self的理解
# 类的默认第一形参
# 判断下面一段代码的运行结果
#
# 要求：
#
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()
#
# <__main__.Test object at 0x0000017D4C11FB48>
# <class '__main__.Test'>
# 在类内定义一个可以重新设置私有属性name的函数，同时条件为字符串长度小于10,才可以修改.
# class Dog:
#     def __init__(self):
#         self.__name = "name"
#         self.str = "name"
#     def change(self):
#         if 10 > len(self.str) > 0:
#             self.__name = "牛兰福"
#         else:
#             return
# dog = Dog()
# dog.change()
# 创建一个动物类,并通过init方法接受参数(name),并打印"init被调用".
# class Animal:
#     def __init__(self, name):
#         self.name = name
# cat = Animal("凯迪")
# print(cat.name)
# 使用动物类，实例化一个dog对象取名"八公"
# class Animal:
#     def __init__(self, name):
#         self.name = name
# dog = Animal("八公")
# print(dog.name)
# 如何理解多继承?
# 一个类可以继承多个类的。优先调用第一个类
# 写出一个简单的多继承案例.
# class GrandFather:
#     def show_a(self):
#         print("我是a")
# class Father:
#     def show_b(self):
#         print("我是b")
# class Son(GrandFather, Father):
#     pass
# son = Son()
# son.show_a()
# son.show_b()
# 如果多个父类中有相同的方法,那么子类在调用的时候,调用哪个?
#  优先调用第一个类
# 如何理解重写?
#  子类与父类重名，子类覆盖父类, 相同继承，相异打印自身
# 下面有一个类,请创建一个子类并重写类中的方法
#  #coding=utf-8
# class Car:
#  def run(self):
#      print("奔驰在路上!")
# class  Bmw(Car):
#     def run(self):
#         print("奔驰在万达广场")
#         pass
# bmw = Bmw()
# bmw.run()
# coding=utf-8
# class Car:
#     @classmethod
#     def run(cls):
#         print("奔驰在路上！")
# car = Car
# car.run()
# 你是如何理解多态的?
# python默认就是多态的
#     所谓的多态：既能调用父类方法，又能调用子类方法
# 请解读出多态一章中python"鸭子类型"程序的运行结果.
# class Father:
#     def doctor(self):
#         print("治病")
# class Son(Father):
#     pass
# class GoldGirl:
#     def ill(self):
#         print("生病")
#         son = Son()
#         son.doctor()
# daughter = GoldGirl()
# daughter.ill()
# 利用继承编写下面一段代码
# 动物:吃,喝,跑,玩
#
# 猫:喵喵叫
#
# 狗:旺旺叫
#
# 猫狗继承于动物,并且有2、3中自己的属性.
#
# 创建猫和狗的对象，并调用可用的所有方法
# class Animal:
#     def __init__(self, cay):
#         self.cay = cay
#     def eat(self):
#         print("吃")
#     def drink(self):
#          print("喝")
#     def run(self):
#         print("跑")
#     def play(self):
#         print("玩")
# class Cat(Animal):
#     def __init__(self):
#         super().__init__(self)
#         self.cay = "喵喵叫"
#     pass
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(self)
#         self.cay = "汪汪叫"
#     pass
# cat = Cat()
# print(cat.cay)
# cat.eat()
# cat.drink()
# cat.run()
# cat.play()
# dog = Dog()
# print(dog.cay)
# dog.eat()
# dog.drink()
# dog.run()
# dog.play()
# 编写一段代码以完成下面的要求
#
# 要求：
#
# 定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
#
# 提供str方法，返回姓名和年龄信息
#
# 将类中的姓名和年龄私有化.
#
# 提供获取私有属性的方法.
#
# 提供可以设置私有属性的方法.
#
# 设置年龄时限制范围(0-100)


# class People:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def change(self, name, age):
#         self.__name = name
#         self.__age = age
#         if 100 >= age >= 0:
#             print(f"{self.__name}{self.__age}岁了")
#         else:
#             print("sorry！")
#
#     def __str__(self):
#         return f"{self.__name}{self.__age}岁了！"
#
#
# people = People("张三", 100)
# people.change("张三", 100)
# print(people)


class Animal:
    def __init__(self, eat, drink, run, play):
        self.eat = eat
        self.drink = drink
        self.run = run
        self.play = play


class Cat(Animal):
    def __init__(self, eat, drink, run, play):
        super(Animal, self).__init__(self, eat, drink, run, play)
        self.action = "喵喵叫"


class Dog(Animal):
    def __init__(self, eat, drink, run, play):
        super(Animal, self).__init__(self, eat, drink, run, play)
        self.action = "旺旺叫"


cat1 = Cat("吃老鼠", "喝牛奶", "边跑边跳舞", "玩皮球")
dog1 = Dog("吃骨头", "喝啤酒", "边跑边喝啤酒", "玩发呆")



