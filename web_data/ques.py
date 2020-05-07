'''In this assignment you will write a Python program that expands on 
http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from 
the data files below, extract the href= vaues from the anchor tags, scan for a tag that is 
in a particular position relative to the first name in the list, follow that link and repeat 
the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for 
your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
 The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Colm.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: M'''

import urllib.error
import urllib.parse
import urllib.request
import bs4
positions = 18
counts = 7
z = "http://py4e-data.dr-chuck.net/known_by_Colm.html"
count = 0
for num in range(counts):
    url = z
    req = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(req, 'lxml')
    single_page = soup.find_all('a')
    count = 0
    print(single_page)
    for a_tag in single_page:
        print(a_tag)
        name = a_tag.text
        print(name)
        link = a_tag.get('href')
        print(link)
        count += 1
        if count == positions:
            z = link
            break
    print('-'*100)
print(name)
