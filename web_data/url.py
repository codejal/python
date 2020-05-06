# function of socket can also be done by urllib
# using urllib is equal to file handler
import urllib.request
import urllib.parse
import urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
