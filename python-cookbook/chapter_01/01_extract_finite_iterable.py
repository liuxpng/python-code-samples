l = [1, 2, 3]
i1, i2, i3 = l
print(i1, i2, i3)

t = (1, 2, 3)
i1, i2, i3 = t
print(i1, i2, i3)

s = 'python'
s1, s2, s3, s4, s5, s6 = s
print(s1, s2, s3, s4, s5, s6)

l = ['a', 'b', 'c', (12, 13)]
_, b, _, d = l
print(b, d)

a, b, c, (d, e) = l
print(a, b, c, d, e)
