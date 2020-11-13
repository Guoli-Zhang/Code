import threading
import os
import time

globals_list = []


def dance(count):
    for i in range(count):
        globals_list.append(i)
        print("跳舞。。。。。", threading.current_thread().name)
        time.sleep(0.5)
    print("dance:", globals_list)


def sing(count):
    for i in range(count):
        print("唱歌。。。。。", threading.current_thread().name)
        time.sleep(0.5)
    print("sing:", globals_list)


if __name__ == "__main__":
    dance_thread = threading.Thread(target=dance, args=(5,), daemon=True)
    sing_thread = threading.Thread(target=sing, kwargs={"count": 5})
    dance_thread.setDaemon(True)

    dance_thread.start()
    # dance_thread.join()
    # print("数据载入中。。。。。")
    sing_thread.start()

    time.sleep(1)
    print("over")
    exit()