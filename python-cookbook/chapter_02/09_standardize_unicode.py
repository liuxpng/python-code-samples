s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1, s2)
print(s1 == s2)

import unicodedata

n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)
print(n_s1, n_s2)
print(n_s1 == n_s2)

n_s1 = unicodedata.normalize('NFD', s1)
n_s2 = unicodedata.normalize('NFD', s2)
print(n_s1, n_s2)
print(n_s1 == n_s2)
