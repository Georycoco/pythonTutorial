# inherit 继承

class Animal:
    def __init__(self):
        self.num = 100
        self.__num2 = 200

    def eat(self):
        print('eating.....')

    def drink(self):
        print('drinking.....')

    def run(self):
        print('running.....')

    def sleep(self):
        print('sleeping.....')

    def test(self):
        print('this is test')

    def __test2(self):  # 私有方法,属性在继承中的表现 都不会被子类继承
        print('this is test2 private')

    def test3(self):
        self.__test2()
        print(self.__num2)


class Dog(Animal):

    def bark(self):
        print('....汪！汪！汪！.....')


class Cat(Animal):

    def catch(self):
        print('....caught a mouse...... ')


class Husky(Dog):

    def bite(self):
        print('....biting furniture......')

    #  方法重写
    def bark(self):
        print('啊～～呜～～～～')
        # 再调用父类里的方法
        # Dog.bark(self)
        super().bark()  # 类似java里的super, 继承上一级父类的方法


wangcai = Dog()
wangcai.eat()

cat = Cat()
cat.catch()

duoduo = Husky()
duoduo.eat()
duoduo.bark()
duoduo.bite()
# duoduo.test2()  私有方法不会被继承
print(wangcai.num)
# print(wangcai.__num2)  私有属性不会继承
wangcai.test3()  # 在一个公有的方法里的私有属性和方法可以被调用


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print('this is test')

    def __test2(self):
        print('this is test2 private')

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):

    def test4(self):
        self.__test2()
        print(self.__num2)


a = B()
a.test3()  # 一个父类中公有的方法里的私有属性和方法可以被子类调用
a.test4()  # 如果在子类中用方法调用父类中的私有方法和属性则不可以
