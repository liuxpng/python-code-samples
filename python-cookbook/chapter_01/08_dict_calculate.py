
prices = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 5,
    'g': 1,
}

print(prices)
print(dict(zip(prices.values(), prices.keys())))

print(min(prices))
print(max(prices))

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

print(sorted(zip(prices.values(), prices.keys())))

print(prices)
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
