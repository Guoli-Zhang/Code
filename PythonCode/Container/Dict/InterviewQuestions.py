# 键值互换

dict_old = {"1": 4, "2": 5, "3": 6}
dict_new = dict([value, key] for key, value in dict_old.items())
dict_New = dict(zip(dict_old.values(), dict_old.keys()))
print(dict_new, dict_New)

# ---
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]

print(f"A0={A0}", end=" ")
print(" ")

print(f"A1={A1}", end=" ")
print(" ")

print(f"A2={A2}", end=" ")
print(" ")

print(f"A3={A3}", end=" ")
print(" ")

print(f"A4={A4}", end=" ")
print(" ")

print(f"A5={A5}", end=" ")
print(" ")

print(f"A6={A6}", end=" ")
print(" ")

# 按值排序
d = {"wd": 23, "gty": 57, "wdd": 25, "uji": 12, "wrt": 34}

print(sorted(d.items(), key=lambda x: x[1]))
