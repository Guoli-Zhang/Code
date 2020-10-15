# encoding:utf-8

a = [1, 2, 3, 4, 5, 6, 7]
b = filter(lambda x: x > 5, a)
for i in b:
    print(i)
a = map(lambda x: x * 2, [1, 2, 3])

print(a)
print(list(a))

# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
nums = range(2, 20)
for i in nums:
    nums = filter(lambda x: x == i or x % i, nums)
print(list(nums))
# >> [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


my_list = ['edward', 'Smith', 'Obama', 'john', 'tom']


def f(x):
    return x[0].isupper()


result = filter(f, my_list)
print(list(result))

# ---
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(x):
    return x % 2 == 0


result = filter(f, my_list)
print(list(result))
