def func_out(fn):
    def func_inner(*args, **kwargs):
        print("启动内部函数！")
        result = fn(*args, **kwargs)
        return result
    return func_inner


@func_out
def summer(a, b):
    result = a + b
    print(result)
    # return result





@func_out
def summer_num(*args, **kwargs):
    result = 0
    for values in args:
        result += values

    for value in kwargs.values():
        result += value

    print(result)


if __name__ == "__main__":
    summer(10, 20)
    summer_num(12, 13, 26, a=10, b=60)