def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    else:
        return fib_recur(n-1) + fib_recur(n-2)


feibo_list = []
for i in range(1, 20):
    feibo_list.append(fib_recur(i))
    print(fib_recur(i), end=" ")
print(feibo_list)
