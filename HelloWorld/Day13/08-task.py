import time


def logging(path):
    def func_out(fn):
        def func_inner(*args, **kwargs):
            begin = time.time()
            if path == "+":
                print("+运算执行中......")
            if path == "-":
                print("-运算中......")
            result = fn(*args, **kwargs)
            end = time.time()
            print(f"运算执行到此共花费{end - begin}s")
            return result
        return func_inner
    return func_out


@logging("+")
def add(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result *= value
    for value in range(101):
        result += value
    print(result)
    return result

@logging("-")
def sub(*args, **kwargs):
    result = 0
    for value in args:
        result -= value
    for value in kwargs.values():
        result /= value
    for value in range(101):
        result += value
    print(result)
    return result



if __name__ == "__main__":
    print(add(10, 25, 38, 40, 11, a=2, b=6, c=2.6))
    print(sub(500, 40, 20, 10, 5, a=10, b=11, c=21))





