# 多继承

# class Base (object) object 表示无论子类有没有添加都将被继承
class Base(object): 
    def test(self):
        print('this is base class')

class A(Base):
    def testA(self):
        print('this is A class')

class B(Base):
    def testB(self):
        print('this is B class')

class C(A,B):
    def testC(self):
        print('this is C class')


c = C()
c.test()


# polymorphism
class Dog(object):
    def test(self):
        print('hello every one~~this is boss here~')

class xiaotian(Dog):
    def test(self):
        print('hello this is xiaotian here')


def introduce(temp):
    temp.test()

dog1 = Dog()
dog2 = xiaotian()

introduce(dog2)
introduce(dog1)