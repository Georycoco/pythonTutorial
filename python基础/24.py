# Object Oriented Programming  面向对象

'''定义一个类 猫'''
class Cat:
    #定义一个init方法,可以初始化对象,每次调用类一定会调用init方法
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def __str__(self): #str 方法，类会自动调用,输出对象信息
        return '%s is %d years old'%(self.name,self.age)

    # 在类中定义方法需要写上 self
    def eat(self): 
        print('lovely food')
  
    def drink(self):
        print('cat is drinking a Coke!')

    def introduce(self):
        #print('%s is %d years old'%(tom.name,tom.age))
        print('%s is %d years old'%(self.name,self.age))
    
#创建一个对象, python 中需要用一个变量来保存
#tom = Cat() 
#tom.drink()
#tom.age = 3 #添加属性
#tom.name = 'Tom'
#tom.name()

#获取对象属性
#print('%s is %d years old'%(tom.name,tom.age))
#tom.introduce()

#新对象
# self 会根据对象自动变换元素指向的对象，哪个对象调用就用哪个对象的元素值
#jiafei = Cat()
#jiafei.name = '加菲'
#jiafei.age = 3
#jiafei.introduce()

#init 的用法
lanmao = Cat('蓝猫',10)
lanmao.introduce()

jiafei = Cat('加菲',3)
jiafei.introduce()

print(lanmao) # __str__会返回lanmao的值，在str的rturn中怎么写就怎么return
print(jiafei)