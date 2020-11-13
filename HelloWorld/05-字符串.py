str1 = "acb-abc-bca"
str2 = str1 + "-faq"
print(str2)
if str1.isalpha():
    print("我是字母！")
else:
    print("goodbye")
print(str1.find("a", 1, 5))
print(str1.rfind("a"))
print(str1.count("a"))
str1.replace("acb", "BIM",1)
str3 = str1.replace("acb", "BIM",1)
print(str3)
list1 = str1.split("-")
print(list1)
print(str1[::-1])