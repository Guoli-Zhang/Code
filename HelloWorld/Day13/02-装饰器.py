def func_out(fn):
    print("装饰器被调用")
    def func_inner():
        # fn()
        print("登录！")
        fn()
    return func_inner


@func_out   # @func_out = 'comment = func_out(comment)'
def comment():
    print("验证")


if __name__ == "__main__":

    commen = func_out(comment)
    commen()
    # comment()



