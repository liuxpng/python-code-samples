l = [1, 2, 3, 4, 5, 6, 7]
print([n for n in l if n > 4])
print([0 if n > 4 else n for n in l])

print(list(filter(lambda x: x > 4, l)))

print(list((n for n in l if n > 4)))

from itertools import compress

l = [1, 2, 3, 4, 5]
b = [False, True, False, True, False, True, True]
print(list(compress(l, b)))
