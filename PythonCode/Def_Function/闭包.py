def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
f1 = print(f1)
f2 = f2
f3 = f3
print(f"{f1},{f2},{f3}")
