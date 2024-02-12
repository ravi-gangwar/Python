from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))


print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4])))



l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]

for x, y in zip(l1, l2):
    print(x, y)

t1, t2, t3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)

print(list(zip(t1, t2, t3)))