# 设计一个4S店的构架

class CarStore(object):

    def __init__(self):
        self.factory = Factory()


def select(self, car_model):
    def order(self, car_model):
        return self.factory.select_by_type


class Factory(object):

    def select_by_type(car_model):
        if car_model == 'QQ':
            return QQ()
        elif car_model == 'greatWall':
            return greatWall()
        elif car_model == 'Ix35':
            return Ix35()


class brand(object):
    def export_price(self):
        pass

    def sale(self):
        pass


class vehicle(object):
    def move(self):
        print('car is moving~~~')

    def music(self):
        print('car is playing music~~~')

    def stop(self):
        print('car is stoping~~~')


class QQ(vehicle):
    pass


class greatWall(vehicle):
    pass


class Ix35(vehicle):
    pass


dealer = CarStore()
car = dealer.order('QQ')

car.move()
car.music()
car.stop()
