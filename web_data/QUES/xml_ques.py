'''Welcome Pranjal Gupta from Using Python to Access Web Data

Extracting Data from XML

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
read the XML data from that URL using urllib and then parse and extract 
the comment counts from the XML data, compute the sum of the numbers in the file.


We provide two files for this assignment. One is a sample file where we give
 you the sum for your testing and the other is the actual data you need to 
 process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_429309.xml (Sum ends with 15)'''

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

url = "http://py4e-data.dr-chuck.net/comments_429309.xml"
uh = urllib.request.urlopen(url)
data = uh.read()
print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
summ = 0
for item in lst:
    number = item.find('count').text
    summ += int(number)
print(summ)
