dict1 = {"name": "zhy", "age": 15}
dict2 = dict1
id(dict2)
print(id(dict1))
print(id(dict2))

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(id(list1))
print(id(list2))
print(id(list3))

num1 = 1
num2 = 1
print(id(num1))
print(id(num2))

list1 = []
while True:
    dict1 = {}
    name = input("请输入您的名字：")
    age = input("请输入您的年龄：")
    dict1["name"] = name
    dict1["age"] = age
    list1.append(dict1)
    print(list1)
