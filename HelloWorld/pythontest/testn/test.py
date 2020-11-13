# 17、1.定义一个Person类
#
# ​ 1)属性:姓名name,体重weight
#
# ​ 2)方法：init方法
#
# 2.创建四个对象（"牛一",60 ; "陈二",55 ; "张三",70 ; "王五",65 ),将这四个对象添加到列表。
#
# 3.获取60-70之间的随机数作为体重标准线（包含60和70）,遍历列表将体重大于等于体重标准线的元素
# 写入健康体重名单health.txt。格式如下：
#
# 姓名:牛一 体重:60 状态:健康
#
# 姓名:张三 体重:70 状态:健康
#
# 姓名:王五 体重:65 状态:健康

# import random
# import os
#
#
# class Person(object):
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# def enter_information():
#     global list_person
#     a = Person('牛一', 60)
#     b = Person('陈二', 55)
#     c = Person('张三', 70)
#     d = Person('王五', 65)
#     list_person = [a, b, c, d]
#
#
# enter_information()
#
# norm_weight = random.randint(60, 70)
# print(norm_weight)
# with open('health.txt', 'w', encoding='utf-8') as h:
#     for i in list_person:
#         if i.weight >= norm_weight:
#             h.write(f'姓名：{i.name} 体重：{i.weight} 状态：健康 \n')


print(" ".join(f"{x}" for x in range(200, 301) if not [y for y in range(2, x) if x % y == 0]))

a = 2
for x in range(3, 101):
    for y in range(2, x):
        if x % y == 0:
            break
        else:
            a += x
    print(x)
print(a)


# result = 0
# for i in range(0, len(a) - 1):
#     result += a[i]
# print(result)











