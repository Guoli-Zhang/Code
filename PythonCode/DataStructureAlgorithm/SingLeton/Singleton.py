# encoding:utf-8

class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


if __name__ == "__main__":
    sing1 = Singleton()
    sing2 = Singleton(object)
    print(sing1, sing2)

# ----


class Singleton(object):
    def foo(self):
        pass


singleton_1 = Singleton()

# from a import singleton_1


# ----


import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


obje1 = Singleton()
obje2 = Singleton()
print(obje1, obje2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()


# ---


def singleton(cls):
    __instance = {}

    def __singleton(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return __singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls, ):
        pass