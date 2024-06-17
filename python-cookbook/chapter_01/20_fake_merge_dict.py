d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

d2 = {
    'a': 11,
    'e': 12,
    'f': 13,
}

from collections import ChainMap

chain_map = ChainMap(d1, d2)
print(chain_map)

print(chain_map['a'], chain_map['b'], chain_map['f'])
chain_map['a'] = 22
print(chain_map)

del chain_map['a']
print(chain_map, 'a' in chain_map)
