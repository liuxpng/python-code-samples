
s1 = 'test.txt'
s2 = 'hello.py'

print(s1.startswith('test'), s1.endswith('txt'))

print(s2.startswith('python'), s2.endswith('py'))

print(s1.startswith(('a', 'b', 'python', 'txt')))
print(s1.endswith(('a', 'b', 'python', 'txt')))
