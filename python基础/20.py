# return multipul values

def test():
    a = 1
    b = 2
    c = 3
    d = 4
    e = [a, b, c, d]
    # return d
    # return [a,b,c,d]
    # return (a,b,c,d)
    return a, b, c, d  # <- 这种方法相当于返回元组


num = test()
print(num)


def divid(a, b):
    aa = a // b
    bb = a % b
    return aa, bb  # 元组


aaa, bbb = divid(12, 4)  # aaa = 3, bbb = 0
print(aaa)
print(bbb)

'''
def 函数():
    psss

def 函数():
    return xxx

def 函数(parameter):
    pass

def 函数(parameter):
    return xxx
'''


# 函数嵌套调用

def test_1(a):
    print('this is test 1')
    return a


def test_2(b):
    print('this is test 2')
    return b


def test_3(c):
    print('this is test 3')
    return c


def test_4():
    test_1(1)
    test_2(2)
    test_3(3)


test_4()


# 函数间的调用嵌套应用，实际开发中可以调用其它的方法
def print_line():
    print('-' * 50)


def print_X_line(a):
    i = 0
    while i < a:
        print_line()
        i += 1


print_X_line(20)


def print_add(a, b, c):
    result = a + b + c
    print('%d+%d+%d=%d' % (a, b, c, result))
    return result


def print_average(a, b, c):
    result = (a + b + c) / 3
    print('Average of: %d,%d,%d is %d' % (a, b, c, result))
    return result


'''  也可以调用之前的方法 
def print_average(a1,b1,c1):
    result = print_add(a1,b1,c1)
    result /= 3
    print('Average of: %d,%d,%d is %d'%(a1,b1,c1,result))
    return result
'''

num1 = int(input('first number: '))
num2 = int(input('second number: '))
num3 = int(input('third number: '))

print_add(num1, num2, num3)
print_average(num1, num2, num3)
