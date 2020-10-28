"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

sort = input("input a string:\n")
letters = 0
space = 0
digit = 0
others = 0
for c in sort:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print(f"char:{letters}\nspace:{space}\ndigit:{digit}\nothers{others}")

