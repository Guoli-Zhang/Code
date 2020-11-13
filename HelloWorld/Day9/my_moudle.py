__all__ = ["fun1", "fun2"]

def fun1():
    print("我是fun1")


def fun2():
    print("我是fun2")
    fun1()


name = "王小五"

if __name__ == "__main__":
    name = "王小六"
