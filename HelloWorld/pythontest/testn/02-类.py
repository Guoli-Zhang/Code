# .定义一个Person类
#
# ​ 1)属性:姓名name,体重weight
#
# ​ 2)方法：init方法
#
# 2.创建四个对象（"牛一",60 ; "陈二",55 ; "张三",70 ; "王五",65 ),将这四个对象添加到列表。
#
# 3.获取60-70之间的随机数作为体重标准线（包含60和70）,遍历列表将体重大于等于体重标准线的元素写入健康体重名单health.txt。格式如下：
#
# 姓名:牛一 体重:60 状态:健康

# 姓名:张三 体重:70 状态:健康
#
# 姓名:王五 体重:65 状态:健康

import random


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def information(self):
        return f"'姓名':{self.name},'体重':{self.weight}"


class Health:
    def __init__(self):
        self.health_weight = random.randint(60, 70)
        self.person_list = []

    def add_person(self, person):
        self.person_list.append(person.information)
        print(self.person_list)

    def remove_person(self):
        for value in self.person_list:
            if value['weight'] < self.health_weight:
                self.person_list.remove(value)
            else:
                return

    # def save_person(self):
    #     with open("")



    # def copration(self):
    #     while True:
    #         self.add_person(self, person)



#
# class Health:
#     def __init__(self):
#         self.health_weight = random.randint(60, 70)
#         self.person_list = []
#
#     def add_person(self, person):
#         self.person_list.append(person)
#         print(self.person_list)
#         for value in self.people_list:
#             if value['weight'] >= self.health_weight:
#                 with open("health.txt", "a") as w:
#                     w.write(value)
#
#     def __str__(self):
#         return f"{'、'.join(self.person_list)}, 状态：健康"
#
#
# person1 = Person("牛一", 60)
# person2 = Person("陈二", 55)
# person3 = Person("张三", 70)
# person4 = Person("王五", 65)
# health = Health()
# health.add_people(person1)
# print(health)

