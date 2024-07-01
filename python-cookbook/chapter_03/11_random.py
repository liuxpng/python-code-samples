import random

print(random.random())

l = [1, 2, 3, 4, 5, 6]
random.shuffle(l)
print(random.choice(l))
print(random.sample(l, 4))
print(random.randint(3, 90))
