import random
win = 3
while True:
    player = int(input("请输入您的拳，石头（1）/剪刀（2）/布（3）:"))
    computer = random.randint(1, 3)
    if computer == 1:
        str1 = "石头"
        print("电脑输出的是：%s" % str1)
    elif computer == 2:
        str2 = "剪刀"
        print("电脑输出的是：%s" % str2)
    elif computer == 3:
        str3 = "布"
        print("电脑输出的是：%s" % str3)
        if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            print("玩家胜利")
            win += 1
            print("玩家胜利的次数是：%d" % win)
            if win == 3:
                break
        elif player == computer:
            print("平局")
        else:
            print("电脑胜利")
