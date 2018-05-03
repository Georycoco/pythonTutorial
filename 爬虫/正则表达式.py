import re
'''
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(pattern1 in string)  # True
print(pattern2 in string)  # False
'''

'''
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(re.search(pattern1, string))
print(re.search(pattern2, string))
'''


#multiple patterns('ran' or 'run')

string ='dog runs to cat'
ptn = r'r[au]n'
print(re.search(ptn, 'dog runs to cat'))
print(re.search(r'r[A-Z]n', 'dog runs to cat'))
print(re.search(r'r[a-z]n', 'dog runs to cat'))
print(re.search(r'r[0-9]n', 'dog r2ns to cat at 3'))
print(re.search(r'r[0-9a-z]n', 'dog runs to cat at 3'))

#所有匹配符的大写都是相反的意思
print(re.search(r'r\dn', 'run r4n'))    #\d 数字
print(re.search(r'r\Dn', 'run r4n'))    #\D != 数字

# 空白符 \t\n\r\f\v
print(re.search(r'r\sn', 'r\nn r4n'))
print(re.search(r'r\Sn', 'r\nn r4n'))
print('r\ta')
print('r\na')

# \W  [a-zA-Z0-9_]
print(re.search(r'r\wn', 'r\nn r4n'))
print(re.search(r'r\Wn', 'r\nn r4n'))

# \b 空格，只对单词开始和技术的空格有效,并且必须只有一个空格  \B则不管几个空格都可以
print(re.search(r'\b runs \b', 'dog runs to cat'))
print(re.search(r'\B runs \B', 'dog  runs  to cat'))
