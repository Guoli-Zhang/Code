"""
企业发放的奖金根据利润提成。
利润(1）低于或等干10万元时，奖金可提10%，
利润高于10万元，低于20万元时, 低于10万元的部分按10%提成，高于10万元的部分，可以提成7.5%;
20万到40万之间时，高于20万元的部分，可提成5%; 40万到60万之间时高于40万元的部分，可提成3%;
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成;
从键盘输入当月利润I，求应发放奖金总数?
"""

# moneyI = float(input("请输入当月利润，单位为万元："))
bonus = 0
profit_list = [100, 60, 40, 20, 10, 0]
royalty_rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

while True:
    moneyI = float(input("请输入当月利润，单位为万元："))
    if moneyI == 0:
        break
    else:
        for i in range(6):
            if moneyI > profit_list[i]:
                beyond_money = moneyI - profit_list[i]
                bonus = bonus + beyond_money * royalty_rate[i]
                income = moneyI + bonus

        print(f"当月应发放奖金的总数为{bonus}万元")
