# -*- coding:utf-8 -*-

import os
import random
import time
import threading
from multiprocessing import Process, Pool, Pipe, Manager, Queue


"""进程(Process(([group [, target [, name [, args [, kwargs]]]]])))"""


# 给子进程指定函数传递参数 Demo：


def pro_func(name, age, **kwargs):
    for i in range(3):
        print(f"子进程正在运行中，name={name}, age={age}, pid={os.getpid()}\n{kwargs}")
        time.sleep(0.2)


if __name__ == "__main__":
    # 创建Process对象
    p = Process(target=pro_func, args=("龟叔", 18), kwargs={"林纳斯": 20})
    # 启动进程
    p.start()
    time.sleep(0.6)
    # 0.6秒钟之后，结束子进程
    p.terminate()
    p.join()



import multiprocessing
# 线程通信=====(队列) ---- from queue import Queue
# 进程池中进程通信=====(队列) --- from multiprocess.Manager import Queue
# 多进程通信=========(队列)   ---- from multiprocess import Queue
import time


def after(conn):
    while True:
        print("接收到数据:", conn.recv())
        time.sleep(1)


def before(conn):
    while True:
        data = [42, None, 34, 'hello']
        conn.send(data)
        print("正在发送数据：%s" % (data))
        time.sleep(1)


def main():
    # send recv
    before_conn, after_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=after, args=(after_conn,))
    p1.start()

    p2 = multiprocessing.Process(target=before, args=(before_conn,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()


# Manager
# manager中的一些数据结构，dict使用（类似共享变量）


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    progress = Manager().dict()
    first_progress = Process(target=add_data, args=(progress, "a", 1))
    second_progress = Process(target=add_data, args=(progress, "b", 2))
    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress)

# # 分布式进程
# # 遇到大型计算任务，一台主机无法完成时，需要多台主机进行计算
#
# # 管理端
# import random
# from queue import Queue
# # BaseManager: 提供了不同机器之间共享数据的一种方法(ip:port)
# from multiprocessing.managers import BaseManager
#
# # 1. 创建存储任务需要的队列
# task_queue = Queue()
#
# # 2. 存储任务执行结果的队列
# result_queue = Queue()
#
# # 3. 将队列注册到网上(使得其他主机也可以访问)
# BaseManager.register('get_task_queue', callable=lambda: task_queue)
# BaseManager.register('get_result_queue', callable=lambda: result_queue)
#
# # 绑定ip和端口， 并且来个暗号；
# manager = BaseManager(address=('172.25.60.250', 4000), authkey=b'westos')
#
# # 4. 启动manager对象， 开始共享队列
# manager.start()
#
# # 5. 通过网络访问共享的Queue对象;
# # BaseManager.register会注册一个方法, 当调用方法时， 执行函数lambda : task_queue;
# task = manager.get(task_queue)  # Bug
# result = manager.get_result_queue()  # Bug
#
# # 6. 往队列里面放执行任务需要的数据;
# for i in range(1000):
#     # 模拟有1000个数字；
#     n = random.randint(1, 100)
#     task.put(n)
#     print("任务列表中加入任务: %d" % (n))
#
# # 7. 从result队列中读取各个机器中任务执行的结果;
# for i in range(1000):
#     res = result.get()
#     print("队列任务执行的result: %s" % (res))
#
# #  8. 关闭manager对象， 取消共享的队列
# manager.shutdown()
#
# # 被管理端1
# import time
# from multiprocessing.managers import BaseManager
#
# # 1. 连接Master端， 获取共享的队列;ip是master端的ip， port'也是master端manager进程绑定的端口;
# slave = BaseManager(address=('172.25.60.250', 4000), authkey=b'westos')
#
# # 2. 注册队列， 获取共享的队列内容;
# BaseManager.register('get_task_queue')
# BaseManager.register('get_result_queue')
#
# # 3. 连接master端;
# slave.connect()
#
# # 4. 通过网络访问共享的队列;
# task = slave.get_task_queue()
# result = slave.get_result_queue()
#
# # 5. 读取管理端共享的任务， 并依次执行;
# for i in range(500):
#     n = task.get()
#     print("slave1 运行任务 %d ** 2: " % (n))
#     res = "slave1: %d ** 2 = %d" % (n, n ** 2)
#     time.sleep(1)
#     # 将任务的运行结果放入队列中;
#     result.put(res)
#
# print("执行结束........")
#
# # 被管理端2
# import time
# from multiprocessing.managers import BaseManager
#
# # 1. 连接Master端， 获取共享的队列;ip是master端的ip， port'也是master端manager进程绑定的端口;
# slave = BaseManager(address=('172.25.60.250', 4000), authkey=b'westos')
#
# # 2. 注册队列， 获取共享的队列内容;
# BaseManager.register('get_task_queue')
# BaseManager.register('get_result_queue')
#
# # 3. 连接master端;
# slave.connect()
#
# # 4. 通过网络访问共享的队列;
# task = slave.get_task_queue()
# result = slave.get_result_queue()
#
# # 5. 读取管理端共享的任务， 并依次执行;
# for i in range(500):
#     n = task.get()
#     print("slave2: 运行任务 %d ** 2: " % (n))
#     res = "slave2: %d ** 2 = %d" % (n, n ** 2)
#     time.sleep(1)
#     # 将任务的运行结果放入队列中;
#     result.put(res)
#
# print("执行结束........")



"""协程"""
