from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.taobao.com/").read().decode('UTF-8') # must decode if page contains chinese
#html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure").read().decode('UTF-8')
#html = urlopen("https://www.taobao.com/").read().decode('UTF-8')
print(html)

#res = re.findall(r'<title>(.+?)</title>', html)
res = re.findall(r'<p>(.*?)</p>', html, flags=re.DOTALL)
print('\nPage title is: ', res)
