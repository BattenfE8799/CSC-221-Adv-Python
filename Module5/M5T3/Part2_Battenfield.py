"""
Beautiful Soup Part 2
CSC 221-0001
Elizabeth Battenfield
12/2/2021
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

#specify new beautiful soup object
nav = soup.nav

#grab links from just the nav bar
for url in nav.find_all('a'):
    print(url.get('href'))
    
#you can grab the body section and the text from there
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

# grab a specific tag from a specific class
for div in soup.find_all('div', class_='body'):
    print(div.text)