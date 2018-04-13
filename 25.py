#  应用 烤地瓜
class SweetPotato:

    def __init__(self):
        self.cookString = 'raw'
        self.cookLevel = 0
        self.condiments = []
    
    def __str__(self):   # self 类似 java 中的 this 谁调用的方法就指向谁
        return 'SweetPotato cook state: %s(%d); Condiments added: %s'%(self.cookString,self.cookLevel,str(self.condiments))

    # 烤地瓜，生熟用 cookLevel表示，0-3 是生的，超过3表示半生，超过5表示熟了，超过8表示焦了
    def cook(self, cooked_time):
        self.cookLevel += cooked_time
        
        if self.cookLevel>=0 and self.cookLevel <=3:
            self.cookString = 'rare'
        elif  self.cookLevel>3 and self.cookLevel <=5:
            self.cookString = 'medium rare'
        elif  self.cookLevel>5 and self.cookLevel <=8:
            self.cookString = 'well done'
        elif  self.cookLevel>8:
            self.cookString = 'charred'
            
    def addSeasoning(self,item):
        self.condiments.append(item)


# 创建一个地瓜对象
def main():
    digua = SweetPotato()

    while True:
        time = int(input('enter a time for cook: '))
        digua.cook(time)
        item = input('enter a seasoning for cook: ')
        digua.addSeasoning(item)
        print(digua)       

main() #start here