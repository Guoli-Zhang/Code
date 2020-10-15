# encoding:utf-8

"""开启"""

import time
start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f"a:{a}, b:{b}, c:{c}")
end_time = time.time()
cost_time = end_time - start_time
print(f"cost_time:{cost_time}")


"""时间复杂度"""

import timeit
def t1():
    list1 = []
    for i in range(5001):
        list1.append(i)

def t2():
    list2 = []
    for i in range(5001):
        list2.insert(0, i)

def t3():
    list3 = []
    for i in range(5001):
        list3 = list3 + [i]

def t4():
    list4 = [i for i in range(5001)]

def t5():
    list5 = list(range(5001))


timer1 = timeit.Timer("t1()", "from __main__ import t1")
timer2 = timeit.Timer("t2()", "from __main__ import t2")
timer3 = timeit.Timer("t3()", "from __main__ import t3")
timer4 = timeit.Timer("t4()", "from __main__ import t4")
timer5 = timeit.Timer("t5()", "from __main__ import t5")

print(f"append:{timer1.timeit(number=100)}")
print(f"insert:{timer2.timeit(number=100)}")
print(f"[] + []:{timer3.timeit(number=100)}")
print(f"[x for x in range(n)]:{timer4.timeit(number=100)}")
print(f"list():{timer5.timeit(number=100)}")
