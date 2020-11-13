def func_out(num1):
    def func_inner(num2):
        nonlocal num1
        num1 = 101
        result = num1 + num2
        print(f"结果是{result}")
    print(num1)
    func_inner(2)
    print(num1)
    return func_inner


def config_name(name):
    def say_info(info):
        nonlocal name
        name = "Jon"
        print(name + ":" + info)
    return say_info





if __name__ =="__main__":
    f = func_out(1)
    f(102)
    f(3)

    Tome = config_name("Tom")
    Jerry = config_name("jerry")
    Tome("Hello?")
    Jerry("I'am here! Tom")
    Tome("Are you OK? I'm Jon")
    Jerry("Sorry, Jon")
    Tome("What's problem?")





