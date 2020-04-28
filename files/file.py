fhandle = open("random.txt", "r")
count = 0
CODE = "hello"

for sentence in fhandle:
    count = count+1
    sentence = sentence.lstrip()
    print(sentence)
fhandle = open("random.txt", "r")
whole = fhandle.read()
print(len(whole))
print(count)
print(whole.lstrip())
print(count)
