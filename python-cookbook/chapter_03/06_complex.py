
a = complex(1, 3)
print(a)
print(a.real)
print(a.imag)
print(a.conjugate())

b = 3 - 4j
print(b)
print(b.real)
print(b.imag)
print(b.conjugate())

print(a + b)
print(a - b)
print(a * b)
print(a / b)

import cmath

print(cmath.sin(a))
print(cmath.cos(b))
print(cmath.tan(a + b))
