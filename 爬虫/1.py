from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('UTF-8')
#html = urlopen("https://www.taobao.com/").read().decode('UTF-8')
print(html)