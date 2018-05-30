# beautifulsoup library
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure").read().decode('UTF-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')
print(all_href)
all_href = [l['href'] for l in all_href]
# 上面的code就是一个for循环，等同与：
# for l in all_href:
#   print(l['href'])

print('\n', all_href)


# CSS/Tag
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("UTF-8")
