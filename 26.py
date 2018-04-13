# 存放家具 --> 将一个 对象添加进另一个对象

class House:
    
    def __init__(self, new_Size, new_Info, new_Location):
        self.size = new_Size
        self.info = new_Info
        self.location = new_Location
        self.area_left = new_Size
        self.item_in_house = []

    def __str__(self):
        msg = 'House Size: %d, Type: %s, Location: %s, \nAvailable area left: %d'%(self.size,self.info,self.location,self.area_left)
        msg += '\nCurrent item in house: %s'%(str(self.item_in_house))
        return msg
    
    def add_Item(self,item):
        #self.area_left -= item.size  #item 指向bed，所以.size返回当前bed的size
        #self.item_in_house.append(item.name)  #直接调用item的值
        self.area_left -= item.get_Size()      #用bed自带的方法去调用size
        self.item_in_house.append(item.get_Name())

#创建床类，添加进House
class Bed:
    
    def __init__(self, new_name, new_size):
        self.name = new_name
        self.size = new_size

    def __str__(self):
        return '%s spend size of area: %d sqm'%(self.name, self.size)

    def get_Size(self):
        return self.size
    
    def get_Name(self):
        return self.name


def main():
    myHouse = House(200, '3 room', 'Melbourne Toorak')
    print(myHouse)
    print('-'*30)
    bed1 = Bed('席梦思',4)
    print(bed1)
    bed2 = Bed('三人床',6)
    print(bed2)

    myHouse.add_Item(bed1)
    myHouse.add_Item(bed2)
    print(myHouse)

main()




