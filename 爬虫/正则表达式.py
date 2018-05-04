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

print(re.search(r'runs\\', 'runs\ to me')) #两个\\ 表示第一个'\'
print(re.search(r'r.n', 'r[ns to me')) #'.'除了 换行'\n' 都可以匹配

print(re.search(r'^dog', 'dog runs to cat'))  # ^ 表示只有当需要匹配的字符在句首才匹配
print(re.search(r'cat$', 'dog runs to cat'))  # $ 表示只有当需要匹配的字符在句末才匹配

print(re.search(r'Mon(day)?', 'Monday Tuesday'))  # ()? 括号内的字符有没有都匹配
print(re.search(r'Mon(day)?', 'Mon Tuesday'))

'''多行匹配'''
string = """
dog runs to cat.
I run to dog.
"""

print(re.search(r'^I', string))
print(re.search(r'^I', string, flags=re.M))   # flags = re.M 让每行变成单独的句子，每行重新匹配

# 0或多次
print(re.search(r'ab*', 'a'))   # （0，1)
print(re.search(r'ab*', 'abbbbbbbb'))  # * 表示重复的字符也计算在内， 即便没有出现，也会匹配剩下的字符

# 1或多次
print(re.search(r'ab+', 'a'))   # None
print(re.search(r'ab+', 'abbbbbbbb'))  # * 表示重复的字符也计算在内， 如果没有出现，则返回为None


# 可选次数
print(re.search(r'ab{2,10}', 'a'))   # {2,10} 出现2到10次范围内
print(re.search(r'ab{2,10}', 'abbbbbbbbbbbbbbbbb'))  # 如果重复超过10次，只显示设定次数内的字符

# Group
match = re.search(r'(\d+), Date:(.+)', 'ID:0124141, Date:Feb/12/2017')
print(match.group())
print(match.group(1)) #分批次显示
print(match.group(2))

match = re.search(r'(?P<id>\d+), Date:(?P<Date>.+)', 'ID:0124141, Date:Feb/12/2017')  # ?P<> 给每个组加上ID
print(match.group())
print(match.group('id')) #分批次显示
print(match.group('Date'))

# 寻找所有匹配
print(re.findall(r'r[ua]n', 'run ran ren'))
print(re.findall(r'(run|ran)', 'run ran ren'))
print(re.findall(r'r[a|u]n', 'run ran ren'))

#replace
print(re.sub(r'r[au]ns', 'catches', 'dog runs to a cat'))

#split 分裂
print(re.split(r'[,;\\.]', 'a;b,c.d\e'))

#complie 将匹配形式编译保存到一个变量，再使用
complied_re = re.compile(r'r[ua]n')
print(complied_re.search('dog runs to cat'))