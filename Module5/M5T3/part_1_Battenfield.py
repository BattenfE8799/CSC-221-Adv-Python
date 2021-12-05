"""
Beautiful Soup Part 1
CSC 221-0001
Elizabeth Battenfield
12/2/2021
"""

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

#getting all paragraph tabs
print(soup.find_all('p'))

#iterate through all the paragraph tabs
for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

#grabs links
for url in soup.find_all('a'):
    print(url.get('href'))
    
#grab text(the full soup)
print(soup.get_text())
