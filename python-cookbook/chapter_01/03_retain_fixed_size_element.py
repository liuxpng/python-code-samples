from collections import deque

queue = deque(maxlen=5)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

queue.append(6)
queue.append(7)
print(queue)

