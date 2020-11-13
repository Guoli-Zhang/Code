def logging(path):
    def func_out(fn):
        print(f"{path}被调用才是闭包！")

        def func_inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            if logging == "+":
                print("--正在努力加法计算--")
            elif logging == "-":
                print("--正在努力减法计算--")
            # result = fn(num1, num2)

            return result
        return func_inner
    return func_out

@ logging("+")
def add(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result *= value
    return result

@ logging("-")
def sub(*args, **kwargs):
    result = 0
    for value in args:
        result -= value
    for value in kwargs.values():
        result *= value
    return result

if __name__ == "__main__":
    result = add(2, 4, 6, 12, a=3, b=5, c=6)
    print(result)
    result = sub(2, 4, 6, 12, a=3, b=5, c=6)
    print(result)


# def inner(num1, num2):
#     if flag == "+":
#         print("--正在努力加法计算--")
#     elif flag == "-":
#         print("--正在努力减法计算--")
#     result = fn(num1, num2)
#     return result
#
#
# return


