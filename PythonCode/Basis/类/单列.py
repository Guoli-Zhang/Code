

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
