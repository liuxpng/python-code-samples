import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 1

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


queue = PriorityQueue()
queue.push(1, 10)
queue.push(2, 9)
queue.push(23, 8)
queue.push(13, 7)
queue.push(32, 6)
queue.push(33, 5)
queue.push(31, 3)
queue.push(38, 10)

print(queue)
print(queue.pop(), queue.pop(), queue.pop(), queue.pop(), queue.pop(), queue.pop(), queue.pop())
