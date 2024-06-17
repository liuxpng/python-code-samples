def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


l = [1, 2, 3, 4, 5, 4, 3, 6, 7]
print(list(dedupe(l)))


def dedupe_v2(items, key=None):
    seen = set()
    for item in items:
        k = item if key is None else key(item)
        if k not in seen:
            yield item
            seen.add(k)


l = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_v2(l, key=lambda x: (x['x'], x['y']))))
