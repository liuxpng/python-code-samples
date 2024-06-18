s = 'YEAH, but no, but YEAH, but no, but YEAH'
print(s.replace('yeah', 'hi'))

import re
print(re.sub(r'yeah', 'hi', s, flags=re.IGNORECASE))

pattern = re.compile(r'yeah', flags=re.IGNORECASE)
print(pattern.sub('hi', s))
