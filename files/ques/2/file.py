fhandle = open("random.txt", "r")
count = 0
for sentence in fhandle:
    count = count+1
    print(sentence.lstrip())

fhandle = open("random.txt", "r")
whole = fhandle.read()
print(len(whole))
print(count)
print(whole.lstrip())
print(count)
