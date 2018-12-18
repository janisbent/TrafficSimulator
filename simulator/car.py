


class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.crashed = False


class Car(Vehicle):
    length = 1

    def __init__(self, speed):
        super(Car, self).__init__(speed)

    def __str__(self):
        return "*" if self.crashed else ">"


class Truck(Vehicle):
    length = 2

    def __init__(self, speed):
        super(Truck, self).__init__(speed)
