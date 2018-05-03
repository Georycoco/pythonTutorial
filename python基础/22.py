# 引用  python 里‘=’就是引用，永远相等
A = [1, 2, 3]
B = A

A.append(4)
print(B)  # 1,2,3,4

# number 是不可变类型 string 也是， 只不过在申明的时候指向了不同的值
# 在python中只有数字，字符串和元组是不可变类型

a = 'Hello'
a = 'World'  # a 指向了不同的值，‘Hello’依然存在，只不过python解释器在发现其没有指向后会删除它

# 字典中可变类的值不能当作key，数字，字符串，元组都可以
# 因为在存储时哈希算法会将值转成另一组值，如果可变类的值发生改变，将无法匹配

# 递归： 在一个函数里调用自己
# 4！ = 4*3*2*1
# 5! = 5*4!  5 的阶乘等于5乘以4的阶乘，以此类推
# 写递归时一定要想清楚具体哪一步不再调用
'''
i = 1
result = 1
while i <= 4:
    result *= i
    i+=1
print(result)
'''
''' 递归代码逻辑
def getNum(num)
    num*getNum(num-1)
getNum(5)
'''


# !!重点
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)  # 返回值给上一个自己方法
    else:
        return num  # 最后一次调用方法时 num - 1 = 0,所以需要if > 1,  else 直接return


print(factorial(10))

# 匿名函数 参数：式子  lambda 仅仅是指匿名，并不是函数名，声明后一般用变量保存
# lambda的式子里不能用运算符，比如print
# 初学者一般特别简单的函数就用lambda
func = lambda a, b: a + b
result = func(1, 2)
print('result = %s' % result)

# lambda 应用
stus = [
    {'Name': 'George', 'Age': 28},
    {'Name': 'John', 'Age': 21},
    {'Name': 'James', 'Age': 26},
    {'Name': 'Shirley', 'Age': 23},
]

stus.sort(key=lambda a: a['Age'])  # 排序
print(stus)


# 高级应用  不要把一个函数写死，调入lambda函数，将来在传入数据时写入lambda运算
def test(a, b, func):
    result = func(a, b)
    print(result)


test(11, 22, lambda x, y: x * y)


#
def test(a, b, func):
    result = func(a, b)
    print(result)


func_new = input('pleae enter a lambda function name: ')
func_new = eval(func_new)
test(11, 22, func_new)

# 其它知识点 交换
a = 4
b = 6

# 1: 加个变量
c = 0
c = a
a = b
b = c

# 2: 计算的方法求对方的值，完成对换
a = a + b  # 10
b = a - b  # 10-6 = 4
a = a - b  # 10-4 = 6

# 3：
a, b = b, a  # 动态语言的特点

e = [100]


def test(num):
    num = num + num
    print(num)


test(e)
print(e)

# 字符串常见操作
myStr = 'Hello world it cast hard'
name = ['george', 'james', 'mars']
content = 'sfa fasdf sfasd fsdaf dsfsd ajlkjkl \te\te\tetw   \gdf\g\gsg sa jf jsdlatpoewj jlsadlew'
myStr.find('world')
myStr.count('o')
myStr_new = myStr.replace('world', 'World')  # 注意list不可变，所以需要一个新的变量来保存改变后的值，replace会替换所有相同元素
name_new = ''
name_new.join(name)

new_contant = content.split()  # 直接什么都不写，会安不可见的字符切割
