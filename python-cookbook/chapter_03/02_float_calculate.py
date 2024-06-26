
a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)

from decimal import Decimal

c = Decimal('4.2')
d = Decimal('2.1')
print(c + d)
print(c + d == Decimal('6.3'))


from decimal import localcontext

e = Decimal(1.3)
f = Decimal(1.7)
with localcontext() as ctx:
    ctx.prec = 6
    print(e / f)
