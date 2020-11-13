ticket = bool(input("请出示您的车票："))
knife = float(input("请验证您刀的长度："))
arrive = bool(input("车是否已到站："))
if ticket == True:
    print("请您进入安检！")
    if knife <= 15:
        print("请您进入候车大厅等候上车！")
    else:
        print("请交出您的刀！")
    if arrive == True:
        print("欢迎乘坐8848号列车！")
    else:
        print("请您在候车大厅耐心等待！")
else:
    print("您好，请您先购票!")

    # 使用if处理丈母娘家闺女，要求
    # "至少有3辆车，并且要有至少2套房，并且要爱她的女儿"，所有条件都满足才打印
    # "能结婚"

car = 3
house = 2

