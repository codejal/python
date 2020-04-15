# stacks
from array import array
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
print(queue, "\n")

# tuples-read only list therefoe cannotbe modified i.e. adding aur deleting etc
point = (1, 2)
print(type(point))
point = (3, 4)+point
print(point)

# we can convert a list in tuple
point = tuple([1, 2, 3])
point = (1, 2, 3)
# we can access itmes similar to list
print(point[2])
# we can unpack similar to list
x, y, z = point

if 10 in point:
    print("present")

# point[0]=any thing would be a mistake becase no editing
# tuples are basically used at places where you want to make sure no changes even by mistake

# swapping var
x = 10
y = 15
x, y = y, x

# defining multiple var in sam line
a, b, c = 10, 100, 1000

# array
# (used when optimization needed and performance is needed)
# here unlike list all the content of one list must be same matching with typecode
array("i", [1, 2, 3, 4])

# sets
# collection with no duplicates
# used for powerful maths that they provide
# accessing items using index is not supported
numbers = [1, 1, 2, 2, 2, 3, 2, 2, 5, 6, 7, 4]
uni = set(numbers)
print(uni)
second = {1, 11, 3, 48}
second.add(10)
second.remove(3)
len(second)
print(second)
print("intersection", uni & second)
print("union", uni | second)
print("difference", uni - second)
print("union-intersection", uni ^ second)
if 1 in uni:
    print("yes")

# dictionary-key value pair
point = {"x": 1, "y": 2}  # or
point = dict(x=1, y=2, z=6)
if "x" in point:
    print(point["x"])
print(point.get("a", 0))  # therefore see for a if not fount return 0
del point["x"]
print(point)
for key in point:
    print(key)
for key, value in point.items():
    print(key, value)
