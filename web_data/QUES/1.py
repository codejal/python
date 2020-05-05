import re
fh = open('1.txt')
su = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        su = su + float(number)

print(su)
