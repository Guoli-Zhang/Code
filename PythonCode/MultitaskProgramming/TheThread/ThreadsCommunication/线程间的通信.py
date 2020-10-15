# 线程通信=====(队列) ---- from queue import Queue
# 进程池中进程通信=====(队列) --- from multiprocess.Manager import Queue
# 多进程通信=========(队列)   ---- from multiprocess import Queue

# ! /usr/bin/evn python3
# --*-- coding: utf-8 --*--

# 1. python多线程

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

# 2、线程间的通信方式–共享变量
# !/usr/bin/evn python3
# --*-- coding: utf-8 --*--

# 线程之间的通信

# 1、线程间的通信方式--共享变量（不推荐）
# 如果是各种数据的时候，也可首选使用共享变量而非queue
# 共享变量的操作并不是线程安全的操作，为了达到预期的效果必须在这些操作上加上一把锁，能够安照预期的效果在线程之间按照顺序进行同步
# 多进程中共享变量是行不通的
# 声明一个全局变量，将这个全局变量在各个线程中使用


# 以模拟简单的爬取文章列表页在获取详情页作一示例
import time
import threading

# 设置全局变量的方式
detail_url_list = []  # 作用：获取文章的列表页并获取文章详情页的url


# (该列表（或全局或全局变量）可以定义在.py文件中，直接from  模块 import  xx （xx.py）--> xx.全局变量）
# from chaper11 import variables  不推荐：from chapter11.variables import detail_url_list
# detail_url_list = variables.detail_url_list

# 这种方式是通过声明全局变量global的方式进行通信，非常原始并且不够灵活
def get_detail_html():
    # 爬取文章详情页
    global detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url():
    global detail_url_list
    while True:
        # 爬取文章列表页
        print("get url started")
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("http://projectstedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)  # 线程1
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()
    start_time = time.time()
    # 当主线程退出的时候，子线程kill掉
    print("last time: {}".format(time.time() - start_time))

# 根据上面进行变形后的程序

# 以模拟简单的爬取文章列表页在获取详情页作一示例
import time
import threading

# 设置引用的方式
detail_url_list = []  # 作用：获取文章的列表页并获取文章详情页的url


# (该列表（或全局或全局变量）可以定义在.py文件中，直接from  模块 import  xx （xx.py）--> xx.全局变量）
# from chaper11 import variables  不推荐：from chapter11.variables import detail_url_list
# detail_url_list = variables.detail_url_list

# 这种方式是通过引用变量参数的方式进行通信，足够灵活
def get_detail_html(detail_url_list):  # 传入引用，较灵活的方法
    # 爬取文章详情页
    while True:
        # global detail_url_list(去掉全局变量）
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):  # 传入引用，较灵活的方法
    # global detail_url_list  (去掉全局变量）
    # 爬取文章列表页
    while True:
        print("get url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectstedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))  # 线程1
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
    start_time = time.time()
    # 当主线程退出的时候，子线程kill掉
    print("last time: {}".format(time.time() - start_time))

# 3、线程间的通信方式–通过Queue模块进行线程间同步
# !/usr/bin/evn python3
# --*-- coding: utf-8 --*--

# 1、线程间的通信方式--通过queue的方式进行线程间同步（推荐）
# 线程间需要通信，使用全局变量需要加锁。
# 使用queue模块，可在线程间进行通信，并保证了线程安全。


# 以模拟简单的爬取文章列表页在获取详情页作一示例
# queue是线程安全，不加锁，效率高，因为queue用了python中的deque() 双端队列，而deque（）则是线程安全的，在字节码的级别上就已经达到了线程安全
from queue import Queue
import time
import threading

# 设置引用的方式
detail_url_list = []  # 作用：获取文章的列表页并获取文章详情页的url


# (该列表（或全局或全局变量）可以定义在.py文件中，直接from  模块 import  xx （xx.py）--> xx.全局变量）
# from chaper11 import variables  不推荐：from chapter11.variables import detail_url_list
# detail_url_list = variables.detail_url_list

# 这种方式是通过引用变量参数的方式进行通信，足够灵活
def get_detail_html(queue):  # 传入引用，较灵活的方法
    # 爬取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):  # 传入引用，较灵活的方法
    # global detail_url_list  (去掉全局变量）
    # 爬取文章列表页
    while True:
        print("get url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectstedu.com/{id}".format(id=i))  # 阻塞等待有空闲空间为止（put，参数block默认为True，阻塞状态,可以设置timeout）
        print("get detail url end")


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))  # 线程1
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()

    # detail_url_queue.task_done()  调用task_done()函数join()函数才会退出，停止退出的作用
    # detail_url_queue.join()  阻塞等待

    start_time = time.time()
    # 当主线程退出的时候，子线程kill掉
    print("last time: {}".format(time.time() - start_time))


# python 多线程中子线程和主线程相互通信
# !/usr/bin/python
# coding:utf8
'''
多线程和queue配合使用，实现子线程和主线程相互通信的例子
'''
import threading

__author__ = "Kenny.Li"

from queue import Queue
import time
import random

q = Queue()


class MyThread(threading.Thread):
    def __init__(self, q, t, j):
        super(MyThread, self).__init__()
        self.q = q
        self.t = t
        self.j = j

    def run(self):
        time.sleep(self.j)
        self.q.put(u"我是第%d个线程，我睡眠了%d秒,当前时间是%s" % (self.t, self.j, time.ctime()))


count = 0
threads = []
for i in range(15):
    j = random.randint(1, 8)
    threads.append(MyThread(q, i, j))
for mt in threads:
    mt.start()
print("start time: ", time.ctime())
while True:
    if not q.empty():
        print(f"{q.get()}")
        count += 1
    if count == 15:
        break

"""
下面对以上代码进行解释：

1，q 是实例化了的队列对象，具有FIFO性。首先定义一个自己的线程类，重写run方法。注意在构造方法中传入q队列，用于接收每个线程需要返回的消息

2，第26行，通过q.put()方法，将每个子线程要返回给主线程的消息，存到队列中。

3，从第31行开始，生成15个子线程，加入到线程组里，每个线程随机睡眠1-8秒（模拟每个线程干活时间的长短不同）

4，第34-35行，循环开启所有子线程

5，第36行，打印开始时间

6，通过一个while循环，当q队列中不为空时，通过q.get()方法，循环读取队列q中的消息，每次计数器加一，当计数器到15时，证明所有子线程的消息都已经拿到了，此时循环停止。
"""