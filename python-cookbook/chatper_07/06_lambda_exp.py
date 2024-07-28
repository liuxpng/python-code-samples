add = lambda x, y: x + y

c = add(1, 3)
print(c)


names = [
    {'name': 'ade', 'age': 10},
    {'name': 'de', 'age': 10},
    {'name': 'zd', 'age': 10},
    {'name': 'et', 'age': 10},
    {'name': 'cf', 'age': 10},
]

a = sorted(names, key=lambda v: v['name'])
print(a)

