import multiprocessing
import time
import os

g_list = []


def dance(count):
    print("dance:", os.getpid())
    print("dance:", multiprocessing.current_process())
    print("dance的父进程编号：", os.getppid())
    for i in range(count):
        g_list.append(i)
        print("add:", i)
        print("跳舞中...")
        time.sleep(0.2)
        # os.kill(os.getpid(), 9)
    else:
        print("任务执行完成！")

    print("dance:", g_list)


def sing(count):
    print("sing:", os.getpid())
    print("sing:", multiprocessing.current_process())
    print("sing的父进程编号：", os.getppid())
    for i in range(count):
        print("唱歌中...")
        time.sleep(0.2)
    else:
        print("任务执行完成")

    print("sing:", g_list)


if __name__ == "__main__":
    print("main:", os.getpid())
    print("main:", multiprocessing.current_process())
    dance_process = multiprocessing.Process(target=dance, name="myprocess", args=(5,))
    sing_process = multiprocessing.Process(target=sing, kwargs={"count": 3})

    dance_process.daemon = True

    time.sleep(0.5)
    print("over")
    # dance_process.terminate()
    exit()


    dance_process.start()
    # dance_process.join()
    sing_process.start()

    print("main:", g_list)

    # exit()