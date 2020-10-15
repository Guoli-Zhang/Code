# -*- coding:utf-8 -*-

import threading

"""线程"""

# 用两个线程，交替打印奇数和偶数(1-100)
# 第一个线程，打印奇数


def threada():
    for i in range(1, 101):
        if i % 2 != 0:
            lockb.acquire()
            print(i)
            locka.release()
            time.sleep(0.2)


# 第二个线程，打印偶数
def threaddb():
    for i in range(1, 101):
        if i % 2 == 0:
            locka.acquire()
            print(i)
            lockb.release()
            time.sleep(0.2)


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()
    ta = threading.Thread(None, threada)
    tb = threading.Thread(None, threaddb)
    locka.acquire()  # 保证a先执行
    ta.start()
    tb.start()
    ta.join()

# python多线程
# ! /usr/bin/evn python3
# --*-- coding: utf-8 --*--

# 该实例反编译来说明函数执行流程
import dis


def add(a):
    a = a + 1
    return a


print(dis.dis(add))

# Python中一个线程对应于C语言中的一个线程（CPython而言）（Python并不一定就慢，视情况而定）
# pypy解释器专门克服gil慢的一种解释器（去gil化）
# GIL使用同一个时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个CPU上
# gil锁会根据执行的字节码或时间片划分适当的释放（python内部实现机制）
# 该实例来说明GIL在某种情况下会自动释放让下一个线程去执行（时间片来回切换）

# 反编译（函数执行流程）同一时刻只有一个线程在CPU上执行
total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for j in range(1000000):
        total -= 1


import threading

threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)

threading1.start()
threading2.start()

threading1.join()
threading2.join()
print(total)

# 对于io操作来说，多线程和多进程差别不大（用两种方法实现Python多线程编写）
# 1、通过Thread类实例化(适用简单的或是线程池)

# 以模拟简单的爬取文章列表页在获取详情页作一示例
import time
import threading


def get_detail_html(url):
    # 爬取文章详情页
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    # 爬取文章列表页
    print("get url started")
    time.sleep(4)
    print("get detail url end")


if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html, args=("",))  # 线程1
    thread2 = threading.Thread(target=get_detail_url, args=("",))  # 线程2
    # thread1.setDaemon(True) #守护线程
    # thread2.setDaemon(True) #守护线程
    start_time = time.time()
    thread1.start()
    thread2.start()
    # thread1.join() #阻塞等待
    # thread2.join() #阻塞等待
    print("last time: {}".format(time.time() - start_time))  # 主线程

# 2、通过集成Thread来实现多线程
import threading
import time


class GetDetailHtml(threading.Thread):
    def __init__(self, name):  # 重写__init__方法
        super().__init__(name=name)  # 调用__init__方法

    def run(self):  # 重写run方法,而非start方法
        print("get detail html")
        time.sleep(2)
        print("get html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):  # 重写__init__方法
        super().__init__(name=name)  # 调用__init__方法

    def run(self):  # 重写run方法，而非start方法(在此可以编写逻辑复杂的程序)
        print("get detail url")
        time.sleep(4)
        print("get url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()  # 阻塞等待回收
    thread2.join()  ##阻塞等待回收
    # 当主线程退出的时候，子线程kill掉
    print("last time: {}".format(time.time() - start_time))

# 线程通信
from queue import Queue  # 线程通信=====(队列)


# 通过queue


def get_detail_html(queue):
    while True:
        queue.put()
        print("get detail html started")
        time.sleep(3)
        print("get detail html end")


def get_detail_url(queue):
    while True:
        print("get detail url started")
        queue.get(1)
        time.sleep(1)
        print("get detail url end")


if __name__ == "__main__":
    url_queue = Queue(maxsize=1000)
    thread2 = threading.Thread(target=get_detail_url, args=(url_queue,))
    thread2.start()
    for i in range(2):
        thread1 = threading.Thread(target=get_detail_html, args=(url_queue,))
        thread1.start()
        # thread1.join()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()

    # thread2.join()
    print(time.time() - start_time)


