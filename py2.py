# stacks
from collections import deque
web = []
web.append(5)
web.append(6)
web.append(7)
print(web)
web.pop()
print(web)

# queue
# for this we know FIFO therefore for poping
# if first element is removed rest all need to shift

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
