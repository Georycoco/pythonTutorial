from urllib.request import urlopen
from bs4 import BeautifulSoup


# CSS/Tag
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("UTF-8")
print('here is the html structure: \n')
print(html)

soup = BeautifulSoup(html, features='lxml')

#month = soup.find_all('li', {'class': 'month'})
#for m in month:
#    print(m.get_text()) # if not us get_text method 'print(m)', the tags will be printed


jan = soup.find_all('ul', {"class": 'jan'})
print('--'*20)
print(jan)
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.get_text())
