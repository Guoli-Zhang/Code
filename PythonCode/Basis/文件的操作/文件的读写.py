

import linecache
# linecache.getline 第一参数是文件名，第二个参数是行编号。如果文件名不能直接找到的话，会从 sys.path 里找。
# 如果请求的行数超过文件行数，函数不会报错，而是返回''空字符串。
# 如果文件不存在，函数也不会报错，也返回''空字符串。

the_line = linecache.getline("crack_click.py", 11)

print(the_line)

# linecache读取并缓存文件中所有的文本，
# 若文件很大，而只读一行，则效率低下。
# 可显示使用循环, 注意enumerate从0开始计数，而line_number从1开始


def getline(the_file_path, line_number):
    if line_number < 1:
        return " "
    for cur_line_number, line in enumerate(open(the_file_path, "rU")):
        if cur_line_number == line_number - 1:
            return line
    return " "


the_line = linecache.getline("crack_click.py", 30)

print(the_line)


#
import os


def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

def get_lines():
    l = []
    with open("file.txt", "rb") as f:
        for eachline in f:
            l.append(eachline)
    return l

if __name__ == "__main__":
    for e in get_lines():
        print("django, flask, rewuests, virtualenv, selenium, celery")

