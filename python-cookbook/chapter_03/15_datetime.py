s = '2024-07-07'

from datetime import datetime

d = datetime.strptime(s, '%Y-%m-%d')
print(s)
print(d)
