import heapq

l = [12, 14, 54, 67, 43, 23, 1, 5, 7, 45]
largest = heapq.nlargest(3, l)
smallest = heapq.nsmallest(3, l)
print(largest, smallest)

l = [
    {'name': 'a', 'price': 43},
    {'name': 'b', 'price': 3},
    {'name': 'c', 'price': 4},
    {'name': 'd', 'price': 49},
    {'name': 'e', 'price': 41},
    {'name': 'f', 'price': 53},
    {'name': 'g', 'price': 23},
]
largest = heapq.nlargest(3, l, key=lambda x: x['price'])
smallest = heapq.nsmallest(3, l, key=lambda x: x['price'])
print(largest, smallest)

nums = [2, 5, 76, 32, 43, 54, 1, 23, 54, 6]
heapq.heapify(nums)
print(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
