list1 = [
    ["腾讯", "阿里巴巴", "网易"],
    ["读书会", "CCTV"],
    ["万达", "京东"],
    ["黑马", "feiQ"]
]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# i = 0
# while i < len(list1):
#     j = 0
#     while j < len(list1[i]):
#         k = 0
#         while k < len(list1[i][j]):
#             print
#             k += 1
#         print(list1[i][j])
#         j += 1
#     print(list1[i])
#     i += 1


import random

school = [[], [], []]
teachers = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王"]
# school[0].append(teachers[0])
# print(school[0])
# print(school)
# school[random.randint(0, 2)].append(teachers[0])
# print(school)
# school[random.randint(0, 2)].append(teachers[0])
# print(school)
# school[random.randint(0, 2)].append(teachers[1])
# print(school)
# school[random.randint(0, 2)].append(teachers[2])
# print(school)
# school[random.randint(0, 2)].append(teachers[3])
# print(school)
# school[random.randint(0, 2)].append(teachers[4])
# print(school)
# school[random.randint(0, 2)].append(teachers[5])
# print(school)
# school[random.randint(0, 2)].append(teachers[6])
# print(school)
# school[random.randint(0, 2)].append(teachers[7])
# print(school)

# for i in range(8):
#     school[random.randint(0, 2)].append(teachers[i])
# print(school)

for i in teachers:
    school[random.randint(0, 2)].append(i)
# print(school)
j = 1
for i in school:
    # print("第 %d 间办公室有：%d" % (school.index(i)+1, len(i)))
    print("第 %d 间办公室有：%d 人" % (j, len(i)))
    # print("该办公室里分别有：%s" % "、".join(i))
    print("该间办公室里分别有：", end="")
    for k in i:
        print(k + ' ', end="")
    print()
    print("----------------------------------")
    j += 1

