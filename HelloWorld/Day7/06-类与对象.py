class Dog:  # 类(大驼峰命名)
    def eat(self):  # 方法
        print("狗在吃东西！")


yellow_dog = Dog()  # 创建对象（new 一个对象 -new Object()).   变量名 = 类名
yellow_dog.eat()   # 调用方法  对象.方法名
yellow_dog.name = "旺财"  # 定义属性.  属性名 = 属性值
print(yellow_dog.name)  # 调用属性

black_dog = Dog()
black_dog.name = "妥妥"
print(black_dog.name)