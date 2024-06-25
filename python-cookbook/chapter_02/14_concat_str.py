s1 = 'a'
s2 = 'b'
s3 = 'c'

print(s1 + ' ' + s2 + ' ' +s3)
print('{} {} {}'.format(s1, s2, s3))
print(' '.join([s1, s2, s3]))
print(' '.join(v for v in [s1, s2, s3]))
print(s1, s2, s3, sep=' ')
