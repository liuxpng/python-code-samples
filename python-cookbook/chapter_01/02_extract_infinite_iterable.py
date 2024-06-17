l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a, b, *c = l
print(a, b, c)

l = ['a', 'b', 'c', 'd', 'e']
a, b, *_ = l
print(a, b)

*_, e = l
print(e)

l = ['python', 1, 2, 3, 4]
name, *i = l
print(name, i)

l = ['hello']
name, *i = l
print(name, i)
