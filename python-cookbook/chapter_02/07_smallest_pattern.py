
pattern = r'\"(.*)\"'
str = 'Hi, i am ..., who are you? "test1" who cares "test2"'
import re
print(re.findall(pattern, str))

pattern = r'\"(.*?)\"'
print(re.findall(pattern, str))
