a, b = 1, 2

a += b
b = a - b
a -= b
print(a, b)

a ^= b
b ^= a
a ^= b
print(a, b)

a, b = b, a
