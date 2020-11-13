# with open("hello.txt", "w") as f:
#     f.write("hello world")
#
# with open("hello.txt", "r") as r:
#     content = r.read()
#     print(content)
#
# with open("hello.txt", "r") as r:
#     content = r.read(14)
#     print(content)
#
# with open("hello.txt", "r") as r:
#     content = r.readlines()
#     for i in content:
#         print(i, end="")

with open("hello.txt", "r") as r:
    while True:
        content = r.readline()
        if content == "":
            break
        print(content, end="")



