import re

pattern = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''

print(re.findall(pattern, text1))
print(re.findall(pattern, text2))

pattern = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(re.findall(pattern, text1))
print(re.findall(pattern, text2))

pattern = r'/\*((?:.|\n)*)\*/'
print(re.findall(pattern, text1))
print(re.findall(pattern, text2))
