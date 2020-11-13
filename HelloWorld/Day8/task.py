# 如何理解面向对象编程(OOP)
# 答：对于面向对象的思想：需要实现一个功能的时候，看中的并不是过程和步骤，而是关心谁帮我做这件事，面向对象的三大特征有：封装性
# 、继承性、多态性。
# 什么是类，什么是对象
# 答：类 ；是对一类具体的事物的抽象的概括，具有相似的内部状态和运动规律的实体的集合，具有相同属性和行为事物的统称，是抽象的；
# 对象：是一个具体的事物，在现实世界中可以看得见摸得着，可以直接使用的。拥有相同（或者类似）属性和行为的对象都可以抽想出一个类。

# python中如何定义一个类
# class 类名：具有属性和行为（方法）的抽象概括

# 类(class)由哪三个部分构成
# 类的三部分：属性、行为、
# 类名的命名规则是什么
# 大驼峰
# python中如何通过类创建对象，请用代码进行说明
# class 类名：
# 如何在类中定义一个方法，请用代码进行说明
# class Dog:
#     def __init__(self):
#         print()
#
#     def eat(self):
#         print()
#
#     def __str__(self):
#         return
#
# 定义一个People类，使用People类，创建一个mayun对象后，添加company属性，值是"阿里巴巴"；创建一个wangjianlin对象，
# 添加company属性，值是"万达集团"
# class People:
#     def company(self):
#         print("阿里巴巴")
# class People:
#     def company(self):
#         print("万达集团")
# ma_yun = People()
# wang_jian_ling = People()
# ma_yun.company()
# wang_jian_ling.company()

# 定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
# class Fruits:
#     def __init__(self, species, colors):
#         self.species = species
#         self.colors = colors
#
#     def __str__(self):
#         return f"{self.colors}的{self.species}"
#
# apple = Fruits("苹果", "红色")
# print(apple)
# orange = Fruits("橘子", "橘黄色")
# print(orange)
# watermelon = Fruits("西瓜", "绿色")
# print(watermelon)

# 定义一个汽车类，并在类中定义一个move方法，然后分别创建BMW_X9、AUDI_A9对象，并添加颜色、马力、型号等属性，然后分别打
# 印出属性值、调用move方法
# class Automobile:
#     def __init__(self, colors, horsepower, model ):
#         self.colors = colors
#         self.horsepower = horsepower
#         self.model = model
#
#     def move(self):
#         print(f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9火力全开奔驰在撒哈拉沙漠！")
#
#     def __str__(self):
#         return f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9奔驰在撒哈拉沙漠！"
#
#
# BMW_X9 = Automobile("红色", "超大马力", "FX86")
# BMW_X9.move()
# print(BMW_X9)

# 要求:
#
# __init__方法有什么作用，如何定义
#  __init__()方法，在创建一个对象时默认被调用，不需要手动调用
# 答：__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去。
#
# __str__方法有什么作用，使用时应注意什么问题
# 答：如果类定义了__str__(self)方法，那么就会打印从在这个方法中 return 的数据
# __str__方法通常返回一个字符串，作为这个对象的描述信息
# 方法中的"self"代表什么
#  答：在类内部获取 属性 和 实例方法，通过self获取；
# 在类外部获取 属性 和 实例方法，通过对象名获取。
# 如果一个类有多个对象，每个对象的属性是各自保存的，都有各自独立的地址；
# 但是实例方法是所有对象共享的，只占用一份内存空间。类会通过self来判断是哪个对象调用了实例方法
#
# 在类中定义__init__和__str__方法时，必须提供形参吗，第一个形参又必须是self吗？为什么？
# 答：通过一个类，可以创建多个对象，就好比 通过一个模具创建多个实体一样，__init__(self)中，默认有1个参数名字为self，
# 如果在创建对象时传递了2个实参，那么__init__(self)中除了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)

# 类就好比一个模型，可以预先定义一些统一的属性或者方法，然后通过这个模型创建出具体的对象
#  True
# 类是抽象的，而对象是具体的、实实在在的一个事物
#   True
# 拥有相同(或者类似)属性和行为的对象都可以抽像出一个类
#  True
# 一个类只能创建出一个对象
#  False
# __init__方法在创建对象时，可以完成一些初始化的操作，完成一些默认的设定
#  True
# 类是抽象的，而对象是具体的、实实在在的一个事物
#  True
# __str__方法可以没有返回值
#  False
# __str__方法可以返回除字符串以外的其他类型的数据
#  False

# 使用__init__方法，重新实现关卡一练习2里的6、7、8题， 以达到在创建对象的同时，就为对象添加对应的属性的目的
# class People:
#     def __init__(self):
#         self.company1 = "阿里巴巴"
#         self.company2 = "万达集团"
#
#     def __str__(self):
#         return f"马云创建了{self.company1}，王健林创建了{self.company2}"
#
# mayun = People()
# print(mayun)
# wangjianling = People()
# print(wangjianling)

# class Fruits:
#     def __init__(self, species, colors):
#         self.species = species
#         self.colors = colors
#
#     def __str__(self):
#         return f"{self.colors}的{self.species}"
#
# apple = Fruits("苹果", "红色")
# print(apple)
# orange = Fruits("橘子", "橘黄色")
# print(orange)
# watermelon = Fruits("西瓜", "绿色")
# print(watermelon)

# class Automobile:
#     def __init__(self, colors, horsepower, model ):
#         self.colors = colors
#         self.horsepower = horsepower
#         self.model = model
#
#     def move(self):
#         print(f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9火力全开奔驰在撒哈拉沙漠！")
#
#     def __str__(self):
#         return f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9奔驰在撒哈拉沙漠！"
#
#
# BMW_X9 = Automobile("红色", "超大马力", "FX86")
# BMW_X9.move()
# print(BMW_X9)

# 为前一题的代码添加__str__方法，以实现当直接打印对象时，能打印出可读性较高的信息

# class People:
#     def __init__(self):
#         self.company1 = "阿里巴巴"
#         self.company2 = "万达集团"
#
#     def __str__(self):
#         return f"马云创建了{self.company1}，王健林创建了{self.company2}"
#
# mayun = People()
# print(mayun)
# wangjianling = People()
# print(wangjianling)

# class Fruits:
#     def __init__(self, species, colors):
#         self.species = species
#         self.colors = colors
#
#     def __str__(self):
#         return f"{self.colors}的{self.species}"
#
# apple = Fruits("苹果", "红色")
# print(apple)
# orange = Fruits("橘子", "橘黄色")
# print(orange)
# watermelon = Fruits("西瓜", "绿色")
# print(watermelon)

# class Automobile:
#     def __init__(self, colors, horsepower, model ):
#         self.colors = colors
#         self.horsepower = horsepower
#         self.model = model
#
#     def move(self):
#         print(f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9火力全开奔驰在撒哈拉沙漠！")
#
#     def __str__(self):
#         return f"{self.colors}{self.model}{self.horsepower}型号的BMW_X9奔驰在撒哈拉沙漠！"
#
#
# BMW_X9 = Automobile("红色", "超大马力", "FX86")
# BMW_X9.move()
# print(BMW_X9)

# 任意定义一个动物类
# 使用__init__方法，在创建某个动物对象时，为其添加name、age、color,food等属性，如“熊猫”，5,“黑白”，66，“竹子”
# 为动物类定义一个run方法，调用run方法时打印相关信息，如打印出“熊猫正在奔跑”
# 为动物类定义一个get_age方法，调用get_age方法时打印相关信息，如打印出“这只熊猫今年5岁了”
# 为动物类定义一个eat方法，调用eat方法时打印相关信息，如打印出“熊猫正在吃竹子”
# 通过动物类分别创建出3只不同种类的动物，分别调用它们的方法，让他们“跑起来”，“吃起来”
# class Animal:
#     def __init__(self, name, age, color, food):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.food = food
#
#     def run(self):
#         print(f"{self.name}在running")
#
#     def running(self):
#         print(f"{self.name}跑起来！")
#
#     def eating(self):
#         print(f"{self.name}吃起来！")
#
#     def get_age(self):
#         print(f"{self.name}eating{self.food}")
#
#     def __str__(self):
#         return f"look!一只毛色{self.color}的{self.age}岁{self.name}正在边跑边吃{self.food}！"
#
#
# panda = Animal("熊猫", 5, "黑白", "竹子")
# panda.run()
# panda.get_age()
# print(panda)
# leopard = Animal("豹子", 6, "花色", "野鹿")
# leopard.running()
# lion = Animal("狮子", 4, "金黄色", "斑马")
# lion.eating()
# print(leopard)
# print(lion)

# 完成课件上的烤地瓜应用
#
# class SweetPotato:
#     def __init__(self, name):
#         self.name = name
#         self.state = "生的"
#         self.total = 0
#
#     def cook(self, time):
#         self.total += time
#         if 3 > self.total >= 0:
#             self.state = "生的"
#         elif 6 > self.total >= 3:
#             self.state = "半生不熟"
#         elif 8 > self.total >= 6:
#             self.state = "熟了"
#         elif self.total > 8:
#             self.state = "糊了"
#
#     def __str__(self):
#         if 6 > self.total >= 0:
#             return f"{self.name}才烤了{self.total}分钟，还是{self.state}，建议再烤烤！"
#         elif 8 > self.total >= 6:
#             return f"{self.name}烤了{self.total}分钟,已经{self.state},可以吃了！"
#         elif self.total >= 8:
#             return f"{self.name}烤了{self.total}分钟，快拿出来，已经{self.state}"
#
#
# sweet_potato = SweetPotato("地瓜")
# sweet_potato.cook(5)
# sweet_potato.cook(2)
# print(sweet_potato)

# 完善烤地瓜应用
# 先实现以下方法：
# cook() : 把地瓜烤一段时间
# addCondiments() : 给地瓜添加配料
# __init__() : 设置默认的属性
# __str__() : 让print的结果看起来更好一些
# 然后实现以下方法：
# auto_addCondiments(): 自动随机添加一种配料
# auto_cook(): 自动烤地瓜，当地瓜烤熟了，自动停止
import random


class SweetPotato:
    def __init__(self, name):
        self.name = name
        self.state = "生的"
        self.total = 0
        self.flavour = ["辣椒酱", "沙拉", "咖喱酱"]

    def cook(self, time):
        time = random.randint(6, 8)
        while True:
            self.total += time
            if 3 > self.total >= 0:
                self.state = "生的"
            elif 6 > self.total >= 3:
                self.state = "半生不熟"
            elif 8 > self.total >= 6:
                self.state = "熟了"
                break
            elif self.total > 8:
                self.state = "糊了"

    def add_flavour(self):
        self.flavour = random.randint[self.flavour]

    def __str__(self):
        if 6 > self.total >= 0:
            return f"加了{self.flavour}的{self.name}才烤了{self.total}分钟，还是{self.state}，建议再烤烤！"
        elif 8 > self.total >= 6:
            return f"加了{self.flavour}的{self.name}烤了{self.total}分钟,已经{self.state},可以吃了！"
        elif self.total >= 8:
            return f"加了{self.flavour}的{self.name}烤了{self.total}分钟，快拿出来，已经{self.state}"


sweet_potato = SweetPotato("地瓜")
sweet_potato.cook(5)
sweet_potato.cook(2)
print(sweet_potato)
