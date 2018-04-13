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