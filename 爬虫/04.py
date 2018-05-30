from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 正则表达式 + beautifulsoup
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode("UTF-8")
print(html)

soup = BeautifulSoup(html, features='lxml')
print("-"*30)
print(soup)

img_links = soup.find_all('img', {"src": re.compile('.*?\.jpg')})
print('_'*50)
for link in img_links:
    print(link['src'])

#course = soup.find_all('a', {'href': re.compile('https://morvan.*')})
course = soup.find_all('a', {'href': re.compile('tutorial[s*]')})
print('_'*50)
#print(course)
for link in course:
    print(link['href'])