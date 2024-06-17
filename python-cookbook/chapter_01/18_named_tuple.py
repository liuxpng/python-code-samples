t = (1, 2, 3, 4, 5)
print(t)

from collections import namedtuple

Some = namedtuple('Some', ['a', 'b', 'c', 'd', 'e'])
t1 = Some(*t)
print(t1)
print(t1.a, t1.b, t1.c, t1.d)
print(t1._replace(a=99))

