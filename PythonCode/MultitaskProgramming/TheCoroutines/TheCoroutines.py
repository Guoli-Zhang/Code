# -*- coding=utf-8 -*-

import time


def work1():
    while True:
        print("--A--")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("--B--")
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == '__main__':
    main()
