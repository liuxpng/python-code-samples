
d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

d2 = {
    'a': 2,
    'b': 3,
    'h': 9,
}

print(d1.keys() & d2.keys())
print(d1.keys() - d2.keys())
print(d1.keys() | d2.keys())

print(d1.items() & d2.items())

print({key:d1[key] for key in d1.keys() & d2.keys()})
