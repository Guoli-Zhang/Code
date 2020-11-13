# with open("enumerate.txt", "w") as w:
#     w.write("import")
#
with open("enumerate.txt", "a") as w:
    w.write("content")
#
with open("enumerate.txt", "r+") as w:
    w.write("index")
    content = w.read()
    print(content)

# with open("enumerate.txt", "w+") as w:
#     w.write("value")
#     content = w.read()
#     print(content)

# with open("enumerate.txt", "a+") as w:
#     w.write("True")
#     content = w.read()
#     print(content)

# with open("enumerate.txt", "a") as w:
#     w.write("One World One Drame")
