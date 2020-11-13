def fun(num):
    print(num)
    if num == 10:
        return 10
    return fun(num + 1)


fun(1)

