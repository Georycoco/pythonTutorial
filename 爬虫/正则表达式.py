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