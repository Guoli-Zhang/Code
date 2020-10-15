# -*- coding:utf-8 -*-

import os
import random
import time
import threading
from multiprocessing import Process, Pool, Pipe, Manager, Queue

# 线程通信=====(队列) ---- from queue import Queue
# 进程池中进程通信=====(队列) --- from multiprocess.Manager import Queue
# 多进程通信=========(队列)   ---- from multiprocess import Queue


# 进程间的通信Demo:
# 写数据进程执行的代码：


def write(queue):
    for value in ["A", "B", "C"]:
        print(f"Put {value} to queue...")
        queue.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(queue):
    while True:
        if not queue.empty():
            value = queue.get(True)
            print(f"Get {value} from queue.")
            time.sleep(random.random())
        else:
            break


if __name__ == "__main__":
    # 父进程创建 Queue，并传给各个子进程：
    queue = Queue()
    pw = Process(target=write, args=(queue,))
    pr = Process(target=read, args=(queue,))
    # 启动子进程 pw，写入:
    pw.start()
    # 等待 pw 结束:
    pw.join()
    # 启动子进程 pr，读取:
    pr.start()
    # 等待 pr 结束:
    pr.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止:
    print(">>\n所有数据都已写入并读完")


class Producer(Process):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        # 将需要通信的数据写入队列中;
        for i in range(10):
            self.queue.put(i)
            time.sleep(0.1)
            print("传递消息内容为%s" % i)


class Consumer(Process):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            time.sleep(0.1)
            recvData = self.queue.get()
            print("接受到另一进程传递的数据: %s" % recvData)
            break


if __name__ == '__main__':
    queue = Queue()
    p1 = Producer(queue)
    c1 = Consumer(queue)
    p1.start()
    c1.start()
    p1.join()
    c1.join()


# 进程池间的通信


def producer(queue):
    print(f"producer进程号：{os.getpid()}")
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    print(f"consumer进程号：{os.getpid()}")
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    # pool中的进程间通信需要使用Manager
    queue = Manager().Queue()
    pool = Pool(3)  # 定义一个进程池，最大进程数3
    # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))
    pool.close()  # 关闭进程池，关闭后pool不再接收新的请求
    pool.join()  # 等待pool中所有子进程执行完成，必须放在close语句之后


# Pipe(管道)
# 1). Pipe管道，进程间通信的方式, l类似于 ls | wc -l;
# 2). Pipe()返回两个连接对象, 分别代表管道的两边;
# 3). 管道通信操作的方法: send(), recv;
# 4). 管道间的通信是双向的， 既可以发送，也可以接收；

def producer(pipe):
    pipe.send("a")
    time.sleep(2)
    print(pipe.recv())


def consumer(pipe):
    time.sleep(2)
    data = pipe.recv()
    pipe.send("b")
    print(data)


if __name__ == "__main__":
    # Pipe实现两进程间通信
    s_pipe, r_pipe = Pipe()
    pool = Pool()
    pool.apply_async(producer, args=(s_pipe,))
    pool.apply_async(consumer, args=(r_pipe,))
    pool.close()
    pool.join()