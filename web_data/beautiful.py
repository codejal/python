'''Scraping Numbers from HTML using BeautifulSoup In this assignment you will
rite a Python program similar to http://www.py4e.com/code3/urllink2.py. 
The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers
 in the file.

We provide two files for this assignment. One is a sample file where we
 give you the sum for your testing and the other is the actual data you 
 need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_429307.html (Sum ends 
with 28)
You do not need to save these files to your folder since your program will 
read the data directly from the URL. Note: Each student will have a distinct 
a url for the assignment - so only use your own data url for analysis.
Data Format
The file is a table of names and comment counts. You can ignore most of the
 data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers
from the tag and sum the numbers.
***************************************************************
'''

import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
url = "http://py4e-data.dr-chuck.net/comments_429307.html"
req = urllib.request.urlopen(url).read()
soup = BeautifulSoup(req, 'html.parser')
print(soup.prettify)
# method1

table = [i for i in soup.find_all('span', class_="comments")]
print(table)
tabl = list()
for i in range(len(table)):
    tabl.append(table[i].text)
print(tabl)
number = 0
total = 0
for i in range(len(tabl)):
    number = int(tabl[i])
    total += number
print(total)
print('-'*100)


# method2

total = 0
number = 0
for data in soup.find_all('span', class_='comments'):
    print(data)
    # print(type(data))
    number = data.string  # ==number=data.text
    print(number)
    # print(type(number))----string or text are equal
    total += int(number)
print(total)
print('-'*100)


# method3
total = 0
number = 0
for data in soup.find_all('span', class_='comments'):
    data = str(data)
    print(data)
    # print(type(data))
    number = re.findall('>([0-9]+)<', data)
    print(number)
    total += int(number[0])
print(total)
print('-'*100)
