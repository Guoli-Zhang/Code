

# 等级判断  0级：0~100, 1级：100~150, 2级：150~300, 3级：300~450, 4级：600
def fun(score):
    list = [100, 150, 300, 450, 600]
    list.append(score)
    list.sort()
    return list.index(score)


li = fun(151)
print(li)
