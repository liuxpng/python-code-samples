import re

s = 'Who are you?'
print(s.find('who'))
print(s.find('Who'))

text1 = '11/27/2012'
print(re.match(r'\d+/\d+/\d+', text1))
print(re.findall(r'\d+/\d+/\d+', text1))
print(re.finditer(r'\d+/\d+/\d+', text1))


pattern = re.compile(r'\d+/\d+/\d+')
pattern.match(text1)
pattern.findall(text1)

for v in pattern.finditer(text1):
    print(v)
