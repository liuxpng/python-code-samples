s = 'hello'

print(s.ljust(10))
print(s.ljust(10, '-'))
print(s.rjust(10))
print(s.rjust(10, '-'))
print(s.center(10))
print(s.center(10, '*'))

print('=============')

print(format(s, '=>10s'))
print(format(s, '=<10s'))
print(format(s, '=^10s'))


