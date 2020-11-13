def product(par1, par2):
    a = 1
    b = 2
    # print("-" * a)
    c = par1(a, b)
    d = par2(a, b)
    result = c * d
    print(result)
    # print("-" * b)


product(lambda a, b: a + b, lambda a, b: a ** b)
product(lambda a, b: a - b, lambda a, b: a / b)
product(lambda a, b: a ^ b, lambda a, b: a % b)

