import multiprocessing
import os
import time

# globals_list = []


def dance(count):
    for i in range(count):
        # globals_list.append(i)
        print("跳舞*****",  multiprocessing.current_process(),  os.getpid(), os.getppid())
        # print("add:", i)
        time.sleep(0.5)
        # os.kill(os.getpid(), 9)
    # print("dance:", globals_list)


def sing(count):
    for i in range(count):
        print("唱歌******", multiprocessing.current_process(), os.getpid(), os.getppid())
        time.sleep(0.5)
    # print("sing:", globals_list)


if __name__ == "__main__":
    dance_process = multiprocessing.Process(target=dance, args=(5,))
    sing_process = multiprocessing.Process(target=sing, kwargs={"count": 5})
    dance_process.daemon = True

    # print("main", os.getpid())
    # print("main", multiprocessing.current_process())

    dance_process.start()
    # dance_process.join()
    sing_process.start()
    # print("main:", globals_list)

    time.sleep(0.5)
    print("Over")
    # dance_process.terminate()
    # exit()