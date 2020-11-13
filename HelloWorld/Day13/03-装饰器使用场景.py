import time

def func_out(fn):
    print("装饰器被调用！")
    def func_inner():
        begin = time.time()
        print("启动内部函数！")
        fn()
        print("外部传入函数被开启")
        end = time.time()
        print(f"函数执行花费了{end - begin}")
    return func_inner

def func_out_two(fn):
    print("装饰器又被调用！")
    def func_inner():
        begin = time.time()
        print("又启动内部函数！")
        fn()
        print("外部传入函数再次被开启")
        end = time.time()
        print(f"这次函数执行花费了{end - begin}")
    return func_inner


@func_out
def foo():
    result = 0
    for i in range(101):
        result += i
        print(result)

@func_out_two
def foo():
    result = 0
    for i in range(201):
        result += i
        print(result)




if __name__ == "__main__":
    foo()
