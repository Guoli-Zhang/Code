from typing import List, Any


def spam():
    yield "first"
    yield "second"
    yield "third"


print(spam)

new_list = []
final_list = []


# def find_keys(now):
#     out = now
#     k = new_list[now]
#
#     temp = 0
#     for m in range(now + 1, k + now + 1):
#         if new_list[m] >= temp:
#             temp = new_list[m]
#             out = m
#     print(out)
#     final_list.append(out)
#     if (now + temp) >= (max - 2):
#         return final_list
#     else:
#         return find_keys(now=out)


# out = find_keys(0)
# print(out)
# print(len(out))


N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

ref = [x for x in range(N)]
change = True
while change:
    change = False
    for i in range(N - 1):
        for j in range((i + 1), min(N, i + 1 + data[i])):
            if ref[i] + 1 < ref[j]:
                ref[j] = ref[i] + 1
                change = True

print(ref[-1])