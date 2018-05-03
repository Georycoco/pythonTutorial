# 隐藏属性

class Dog:

    def set_Age(self, new_age):
        if 0 < new_age <= 30:
            self.age = new_age
        else:
            print('illage age, age will be 0')
            self.age = 0

    def get_Age(self):
        return self.age

    def test(self):
        print('-' * 20)

    def __test1(self):  # __ 定义私有方法 ，类似java private
        print('-' * 20)

    def send_message(self, credit):  # 这里判定，满足条件后调用私有方法
        if credit > 10:
            self.__send_message()
        else:
            print('not enough credit, please recharge.')

    def __send_message(self):  # 实际开发中，核心接口不让别人随便调用，定义成私有，用上面的判定方法在类内调用
        print('message sending...')

    def __del__(self):  # 当没有指向的时候，python会自动调用del方法
        print('----Game Over----')


dog = Dog()
dog.age = 3
dog.name = 'Doggie'

# 尽量使用这种方法来设置对象的值,这样可以在赋值时给输入的值添加条件
dog.set_Age(10)

# dog.set_Name()
# age = get_Age()
print(dog.get_Age())

# private method
dog.test()
# dog.__test1()  #在类外无法调用

dog.send_message(100)

dog2 = dog

del dog
del dog2  # dog2 被删除后，没有引用，python自动调用 del 方法, 打印 game over
# 如果不删除 dog2, 在程序结束后还是会调用 del，所以还是会打印 game over
print('-' * 30)

'''
import sys

sys.getrefcount() 查看一个对象的引用个数
'''
