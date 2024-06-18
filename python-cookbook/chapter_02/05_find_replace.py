s = 'yeah, but no, but yeah, but no, but yeah'
print(s.replace('yeah', 'hi'))

import re
print(re.sub(r'yeah', 'hi', s))

pattern = re.compile(r'yeah')
print(pattern.sub('hi', s))
