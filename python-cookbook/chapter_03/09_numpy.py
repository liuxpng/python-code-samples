a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a * 2)
print(a + b)

import numpy as np

c = np.array(a)
d = np.array(b)
print(c)
print(d)
print(c + 2)
print(c * 2)
print(c + d)
print(np.sqrt(c))

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)

e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(e[1])
print(e[:, 3])
