from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random


base_url = 'https://baike.baidu.com'
history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"]  #[item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB]
url = base_url + history[-1]
html = urlopen(url).read().decode('UTF-8')
print(html)
print('_'*50)

soup = BeautifulSoup(html, features='lxml')
print(soup)
print('_'*50)

keywords = soup.find_all('meta', {'content': re.compile('.*?')})
print(keywords)