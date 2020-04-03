print("helloerfwrfwr WORLD ")
print('*'*10)
x = 3
y = 7
print(x+y)

# making my own function


def lello(first, last):
    print(f"i M {first} {last} THE BEST ")


course = "                 gupta                "
lello("pranjaluweygfvjwjhbv", course.lstrip())
pranjal = "HELLO"
print(pranjal)

# multiple argument from single parameter


def multiply(*numbers):
    factor = 1
    for number in numbers:
        factor *= number
    return factor


print(multiply(2, 3, 4, 5, 6))
# lists

lisst = [1, 2, 3, 4, "a", "b"]
zeros = [0]*5
combined = lisst+zeros
print(combined)

# we can combine list containing any type of data
# list function is itreable
auto_list = list(range(20))
chars = list("hello world")
print(len(chars))

# accessing elements of list
letters = ["a", "b", "c", "d", "e"]
# for last element
print(letters[-1])
# changing content of list
letters[0] = "A"
print(f"letters= {letters}")
# slicing
print(letters[0:3])
print(letters[:])
print(letters[:3])  # all elements from index=0m to mentioned
print(letters[1:])  # for elemest from index=1 to last
print(letters[::2])  # for increment of 2
print(letters[::-1])  # for reversed

# unpacking list
# to asssign different elements of list to diff variables
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# also above is equal to
first, second, third = numbers  # in this no of var =no of content

# if we dont want to assiging all elements to variable we can use
numbers = [1, 2, 3, 4, 5, 6, 7]
# packing many elements in a new list
first, second, third, *others = numbers
print(f"first ={first} second = {second} .... rest all elem={others}")

# when we use'*'as a prefix python will pack all the arbitary argument in a list

# loop over list
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# if we use for letters in enumerate(letters)
# we will get tupples(list of index , content) with index

print("using enumerate in for loop to gets tuples(index,content)\n ")

for letter in enumerate(letters):
    print(f"direct print will give tuples={letter} ")
    print(
        f"print content of list letter : index= {letter[0]},content={letter[1]}")

print("using unpacking direct in for loop\n")
for index, letter in enumerate(letters):
    print(index, letter)

# adding or removing new items to a list
print(f"adding elements in list = {letters} ")
letters.append("k")
print(f"using append adding at last ={letters}")
letters.insert(3, "l")
print(f"using insert adding at given position 3={letters}")
print("\nremoving elements \n")
letters.pop()
print(f"removing using pop directly ={letters} ")
letters.pop(2)
print(f"removing using pop with a given index 2={letters}")
# remove only the first element if multiple copies are present
letters.remove("l")
print(f"removing specific letter l using remove ={letters}")
del letters[0:1]
print(f"deleting a range using del command ={letters}")


# finding elements in list if dont exist we get error
letters = ["a", "b", "c", "d", "e", "f"]
print("\nfinding elements in list \n")
print("printing index of given content")
print(letters.index("e"))
# to prevent error
if "s" in letters:
    print(letters.index("s"))
else:
    print("s is not in list letters ")
print("to have no of occurences of a content in the list")
letters.append("d")
print(letters.count("d"), letters)

# sorting
numbers = [90, 56, 78, 56]
numbers.sort()
print(f"\nsorted numbers = {numbers}")
numbers = [90, 56, 78, 56]
numbers.sort(reverse=True)
print(f"sorted numbers inrerverse = {numbers}")
# if we dont want to change original list then
numbers = [90, 56, 78, 56]
newlist = sorted(numbers)
print(numbers, newlist)

# if we are dealing with tuples
items = [
    ("product3", 12),
    ("product2", 9),
    ("product1", 10)
]


# here our basic sorting technique will not work therefore
# method 1
def sort_item(item):
    return item[1]


items.sort(key=sort_item)  # here we are pasiing referenced to our function
print(f"method 1 {items}")
items = [
    ("product3", 12),
    ("product2", 9),
    ("product1", 10),
]
# method 2 lamda function lambda parameter:expression
items.sort(key=lambda item: item[1])
print(f"method 2 {items}")
# if we only want price we create new list by
items = [
    ("product3", 12),
    ("product2", 9),
    ("product1", 10),
]  # map(function,iterable)
price = list(map(lambda item: item[1], items))
print(f"prices={price}")
filtered = list(filter(lambda item: item[1] >= 10, items))
print(f"filtered list ={filtered}")
filtered.sort(key=lambda item: item[1])
print(f"filtered and arranged ={filtered}")

items = [
    ("product3", 12),
    ("product2", 9),
    ("product1", 10),
]
# comprehansion same result as 169
price = [item[1] for item in items]
# comprehansion same result as 171
filtered = [item for item in items if item[1] >= 10]
print(f"using comprehension price={price}filtered={filtered}")

# zip function-make tuples of given list
list1 = [1, 2, 3, 4, 6, 7]
list2 = [10, 20, 30, 40]
zippedlist = (list(zip("abcd", list1, list2, list1)))
