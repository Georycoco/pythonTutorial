from urllib.request import urlopen

html = urlopen("https://www.ebay.com.au/").read().decode('UTF-8')
#html = urlopen("https://www.taobao.com/").read().decode('UTF-8')
print(html)