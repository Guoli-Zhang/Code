# 使用多任务模拟边做饭边听歌的过程（print函数输出过程即可）：
#
# 要求1:做饭和听歌同时进行；
#
# 要求2:做饭分为炒菜和炖汤，因为炖汤时间比较长，可以在炖汤的过程中炒菜；
#
# 要求3:等到菜炒好了，汤也炖好了，关闭音乐。


import multiprocessing
import time


def cook():
    print("做饭")
    print("炖汤")
    time.sleep(0.5)


def listen():
    print("听歌")
    time.sleep(0.5)


if __name__ == "__main__":

    cook_process = multiprocessing.Process(target=cook,)
    listen_process = multiprocessing.Process(target=listen,)
    cook_process.daemon = True

    cook_process.start()
    listen_process.start()