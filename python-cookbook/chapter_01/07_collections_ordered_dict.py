from collections import OrderedDict
import json

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

dd = {}
dd['a'] = 1
dd['b'] = 2
dd['c'] = 3
dd['d'] = 4

print(json.dumps(d))
print(json.dumps(dd))
