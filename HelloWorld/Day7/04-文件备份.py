while True:
    file_name = input("文件名：")
    if file_name == "quit":
        break
    new_name = file_name[:file_name.rfind(".")] + "-副本" + file_name[file_name.rfind("."):]

    with open(file_name, "r") as r:
        content = r.read()

    with open(new_name, "w") as w:
        w.write(content)



# with open("index.txt", "w", encoding=:
