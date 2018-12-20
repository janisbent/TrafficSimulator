


class Vehicle:
    crash_acc = 10

    def __init__(self, speed, pos=0, crashed=False, gran=.5):
        self.speed = speed
        self.crashed = crashed
        self.pos = pos
        self.gran = gran

    def drive(self, sit):
        if self.crashed and self.speed > 0:
            self.speed = max(0, self.speed - (self.crash_acc * self.gran))
        self.pos += int(self.speed * self.gran)

    def crash(self):
        self.crashed = True


class Car(Vehicle):
    length = 15

    def __init__(self, speed):
        super(Car, self).__init__(speed)

    def __str__(self):
        return "*" if self.crashed else ">"


class Truck(Vehicle):
    length = 30

    def __init__(self, speed):
        super(Truck, self).__init__(speed)
