def make_div(fn):
    print("div装饰器")
    def func_inner():
        print("div的内部函数")
        return "<div>" + fn() + "<div>"
    return func_inner


def make_p(fn):
    print("p装饰器")
    def func_inner():
        print("p的内部函数")
        return "<p>" + fn() + "<p>"
    return func_inner


@make_div
@make_p
def python():
    print("python的外部函数")
    return "<html>" + "人生苦短，我用Python!" + "<html>"


if __name__ == "__main__":
    result = python()
    print(result)
