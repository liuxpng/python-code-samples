def f(x, y, z, w):
    print(x, y, z, w)


from functools import partial


f1 = partial(f, 5)
f1(3, 4, 5)


f2 = partial(f, w='w')
f2(1, 2, 3)
