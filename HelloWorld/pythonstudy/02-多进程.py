import time
# 引入进程模块
import multiprocessing


def dance():
    for i in range(5):
        print("唱跳....")
        time.sleep(0.5)


def sing():
    for i in range(5):
        print("rap....")
        time.sleep(0.5)


if __name__ == "__main__":
    # 创建子进程
    dance_pro = multiprocessing.Process(target=dance)
    sing_pro = multiprocessing.Process(target=sing)

    # 启动进程
    dance_pro.start()
    sing_pro.start()

    # dance_pro.run()
    # sing_pro.run()


