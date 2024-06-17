prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

subset = {k: v for k, v in prices.items() if v > 30}
print(subset)

subset_tuple = [(k, v) for k, v in prices.items() if v > 30]
print(subset_tuple)

p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
