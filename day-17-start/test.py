class Car:
    def build_my_car(self):
        self.seats = 2

my_car = Car()
my_car.build_my_car()
print(my_car.seats)

class Car1:
    def __init__(self):
        self.seats = 2

my_car1 = Car1()
print(my_car1.seats)