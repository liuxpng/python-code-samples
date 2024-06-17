l = [1, 2, 3, 4, 5, 6]
print(sum(v for v in l if v > 4))
print(sum(v * v for v in l))

print(min(v for v in l if v > 2))
print(max(v for v in l if v > 3))
