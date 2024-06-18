s = 'hello python how about python'
print(s.split(' '))

s = 'hello, python; how!    about python'

import re

print(re.split(r'[,;!()]\s*', s))

print(re.split(r'(,|;|!)\s*', s))
