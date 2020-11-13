# import threading
#
# g_num = 0
# lock = threading.Lock()
#
#
# def sum_num1():
#     lock.acquire()
#     for i in range(10000000):
#         global g_num
#         g_num += 1
#     print("sum_num1:", g_num)
#     lock.release()
#
#
# def sum_num2():
#     lock.acquire()
#     for i in range(10000000):
#         global g_num
#         g_num += 1
#     print("sum_num2:", g_num)
#     lock.release()
#
#
# if __name__ == "__main__":
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     first_thread.start()
#     second_thread.start()
#
#     first_thread.join()
#     second_thread.join()
#     print("main:", g_num)



# import threading
# import time
#
# lock = threading.Lock()
#
#
# def get_index(index):
#     lock.acquire()
#     print(threading.current_thread())
#     you_list = [1, 0, 0, 8, 6, 1, 0, 0, 8, 5, 6,2, 0, 6, 0, 0, 7, 2, 5, 5, 4, 2, 8]
#     if index >= len(you_list):
#         print("已越界！", index)
#         lock.release()
#         return
#     value = you_list[index]
#     print("value:", value)
#     time.sleep(0.6)
#     lock.release()
#
#
# def get_value(index):
#     lock.acquire()
#     print(threading.current_thread())
#     my_list = [1, 2, 3, 1, 5]
#     if index >= len(my_list):
#         print("已越界！", index)
#         lock.release()
#         return
#     value = my_list[index]
#     print("value:", value)
#     time.sleep(0.6)
#     lock.release()
#
#
# if __name__ == "__main__":
#     for i in range(30):
#         sub_thread = threading.Thread(target=get_value, args=(i,))
#         sub_thread1 = threading.Thread(target=get_index, args=(i,))
#         sub_thread.start()
#         sub_thread1.start()

# from gevent import monkey
# import gevent
# import threading
# import time
#
#
# def dance():
#     for i in range(5):
#         print("跳舞。。。。。")
#         time.sleep(0.5)
#
#
# def sing():
#     for i in range(5):
#         print("唱歌。。。。。")
#         time.sleep(0.5)
#
#
# if __name__ == "__main__":
#     g1 = gevent.spawn(target=dance)
#     g2 = gevent.spawn(target=sing)
#
#     # sunt_thread0.start()
#     # sunt_thread1.start()
#
#     gevent.joinall([g1, g2])
#     # g1.join()
#     # g2.join()


from gevent import monkey
import gevent
import random
import time

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])






