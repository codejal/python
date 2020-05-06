# function of socket can also be done by urllib
# using urllib is equal to file handler
import urllib.request
import urllib.parse
import urllib.error
import re
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = 0
alll = dict()
for line in fhand:
    # print(line)
    words = line.decode().split()
    # print(words)
    #word = line.split()
    for word in words:
        count += 1
        alll[word] = alll.get(word, 0)+1
    print("\n")
print(count, "words in total")
print(alll)
'''
line 9 - we get line wise text from fhand in byte form

line 11 - we decode line to convert it to string from byte and create a list 
called words having individual words
 
line 14 - we itterate through our list words having word each time 

line 16 - in dictionary 'alll' with key as word we get value of word if present
          else it is put to default as 0 then we plus one for each occurence

'''

print("\n\n")
# to extract data from the web page using regular expressions
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = 0
alll = dict()
for line in fhand:
    print(line)
    words = line.decode()
    focus = re.findall('^Ari..*', words)
    print(focus)
