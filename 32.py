class Dog(object):
    # __init___（）方法初始化对象，__new__（）方法创建对象
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        print('string method')
        return 'describtion of method'

    def __new__(cls):
        print('new method...')
        return object.__new__(cls)


a = Dog()
a.__str__()


# 单例对象  无论创建几个对象，指向的对象是同一个
class Car(object):
    __instance = None

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # return 上一次创建的对象的引用
            return cls.__instance

    def __init__(self, name):
        self.name = name


b = Car('dabao')  # 此时如果再往两个对象的name 里输入不同参数，会报错, 必须在new方法里加上name元素
c = Car('xiabao')
print(id(b))
print(id(c))  # 打印出的id结果相同


# 只初始化一次对象
class Car(object):
    __instance = None
    __init_flag = False

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # return 上一次创建的对象的引用
            return cls.__instance

    def __init__(self, name):
        if Car.__init_flag == False:
            self.name = name
            Car.__init_flag = True


b = Car('dabao')
c = Car('xiabao')
