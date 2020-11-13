# 提示用户循环录入字符串，直到输入的字符串以's'结尾时结束录入，将录入的字符串存入列表，遍历列表，
# 将列表中以'a'开头的字符串打印到控制台。

list1 = []
list2 = []
while True:
    str1 = input("请您输入字符串：").strip()
    if str1[len(str1) - 1] == "s":
        break
    else:
        list1.append(str1)
for i in list1:
    if i[0] != "a":
        continue
    else:
        list2.append(i)
print(f"{'、'.join(list2) }")





