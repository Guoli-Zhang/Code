
import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')

print(a, b, c, d)

a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1

print(a)
