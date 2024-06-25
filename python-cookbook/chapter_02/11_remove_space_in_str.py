
s = '   hello world    \n \r \t'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '------hello======'
print(s)
print(s.strip('-'))
print(s.strip('='))
print(s.strip('-='))
print(s.lstrip('-'))
print(s.rstrip('='))
