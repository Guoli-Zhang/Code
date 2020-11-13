# with open("test.txt", "r") as r:
#     content = r.read()
#     print(content)
#
# with open("test.txt", "w") as w:
#     w.write("wow,so beautiful!")

with open("gai lun.txt", "w", encoding="utf-8") as w:
    w.write("德玛西亚！人在塔在！")

with open("gai lun.txt", "r", encoding="utf-8") as r:
    content = r.read()
    print(content)

file_name = "gai lun.txt"
print(file_name[:file_name.rfind(".")])
print(file_name[file_name.rfind("."):])
new_name = file_name[:file_name.rfind(".")] + "-副本" + file_name[file_name.rfind("."):]
print(new_name)

with open(new_name, "w", encoding="utf-8") as w:
    w.write(content)


with open("gai lun-副本.txt", "r", encoding="utf-8") as r:
    content = r.read()
    print(content)
