# 类属性，实例属性

class Tool(object):
    # 类属性
    num = 0  # 这个属性为类属性

    # 实例方法
    def __init__(self, new_name):
        # 实例属性
        self.name = new_name
        Tool.num += 1  # 每创建一次类对象就增加一次计数

    def test(self):
        print('this is test for tool')

    # 类方法，加上 @classmethod,不写self，写cls
    @classmethod
    def add_num(cls):
        cls.num = 100  # 修改类属性

    # 静态方法,在类里面，但跟类没有直接的关系 可以不写任何参数，
    @staticmethod
    def test2():
        print('.............')
        print('...       ...')


tool1 = Tool('铁铲')
tool2 = Tool('工兵铲')
tool1 = Tool('刨子')

tool1.test()  # 用对象名字调用实例方法
Tool.add_num()  # 直接用类名字调用类方法
tool1.add_num()  # 对象也可以调用
print(Tool.num)
Tool.test2()
tool1.test2()
