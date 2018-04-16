# Exception handling

try:
    open('fa.txt')
    print('this is a demo')

except NameError:
    print('error, please check ')

except FileNotFoundError:
    print('no such file,please check')

# python3 必须用括号组成元组，python2 不用
except (FileExistsError, FileNotFoundError, NotADirectoryError):
    print('Erro, please check...')

except Exception as ret:  # Exception 表示上面的except没有捕获到特定的异常，这个Exception一定会捕获到, as ret表示出错的地方
    print('Not sure what the error is')
    print(ret)
else:
    print('execute when there is no error')
finally:
    print('last step no matter there is error or not, execute after exception handling')
print('------end-------')


# 自定义 异常
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


try:
    s = input('please enter:')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)

except ShortInputException as result:
    print('ShortInputException: not enough length, enter length: %d, minimum length: %d'%(result.length,result.atleast))
else:
    print('No exception')

# 异常处理中 再抛出异常
