
"""反转字符串"""

print("aStr" [::-1])

"""将字符串"k:1|k1:2|k2:3|k3:4"，处理成 Python 字典：{k:1， k1:2， ... } # 字典里的 K 作为字符串处理"""
str1 = "k:1|k1:2|k2:3|k3:4"


def str2dict(str1):
    dict1 = {}
    for iterms in str1.split("|"):
        key, value = iterms.split(":")
        dict1[key] = value
    return dict1


result = str2dict(str1)
print(result)
