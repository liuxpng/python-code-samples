
l = [
    'a', 'b', 'c', 'd', 'e', 'f',
    'a', 'b', 'c', 'd', 'e', 'f',
    'a', 'b', 'c', 'd', 'e', 'f',
    'a', 'b', 'c', 'd', 'e', 'f',
    'a', 'b', 'c', 'd', 'e', 'f',
    'a', 'b', 'c', 'd', 'e', 'f',
]

from collections import Counter

a_counter = Counter(l)
print(a_counter.most_common(3))

b_counter = Counter(l)
print(b_counter.most_common(4))

print(a_counter + b_counter)
print(a_counter - b_counter)
