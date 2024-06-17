import collections

d = collections.defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['c'].append(4)

print(d, dict(d))

dd = {}
dd.setdefault('a', []).append(1)
dd.setdefault('b', []).append(3)

print(dd)
