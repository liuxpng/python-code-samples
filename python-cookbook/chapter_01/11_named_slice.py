
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l[2:6])

a_slice = slice(2, 6)
print(a_slice.start, a_slice.stop, a_slice.step)
print(l[a_slice])

b_slice = slice(3, 109)
print(b_slice.indices(len(l)))
