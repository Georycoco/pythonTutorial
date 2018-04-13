#   参数 

def add(a,b):
    result = a + b;
    print('%d + %d = %d'%(a,b,result))


numa = int(input('please enter first number: '))
numb = int(input('please enter second number: '))

add(numa,numb)

# return

def get_tempture(a):
    #tempture = a;
    print('current tempture is: %d'%a)
    return a

#temp = get_tempture()
def get_tempture_fahrenheit(a):
    fahrenheit = (a/5)*9
    print('current fahrenheit tempture is: %d'%fahrenheit)



get_tempture(20)
get_tempture_fahrenheit(30)

#缺省参数   类似java过载

def test(a,b=22):
    result = a + b
    return result

print(test(11))
print(test(3,5))


def test2(a=0,b=22,c=33):
    result = a + b + c
    return result
print(test2(1)) # 56
print(test2(1,2,3)) # 6
print(test2(1,c=3)) # 26

#不定长参数 
def sum(a,b,*args):  # 可以在后面无限加入要运算的值
    result = a+b
    return result

print(sum(1,2,3,4,5,6,7,87,8,2))

def sum(a,b,*args,**kwargs):  # 可以在后面无限加入要运算的值
    result = a+b
    for num in args:
        result+=num
    
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print(result)
    return result

sum(1,2,3,4,5,6,7,8,cost=9,task=10)


#拆包
def demo(a,b,*args,**kwargs):  # 可以在后面无限加入要运算的值
    result = a+b
    for num in args:
        result += num
    print(args)
    print(kwargs)
    print(result)
    return result
A = (111,222,333)
B = {'Name':'George','Age': 28}
C = {'Name':'John','Age': 28}
print(demo(1,2,3,4,5,6,7,8,9,*A,**B))  #  如果 A,B 不赋值或者加*会直接加入args

