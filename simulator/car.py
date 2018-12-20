

# TODO: docstring
class Vehicle:
    crash_acc = 10

    def __init__(self, speed, lane, dist=0, crashed=False, gran=.5):
        self.speed = speed
        self.crashed = crashed
        self.dist = dist
        self.gran = gran
        self.lane = lane

    def drive(self, sit):
        # TODO: Handle situation
        if self.crashed and self.speed > 0:
            self.speed = max(0, self.speed - (self.crash_acc * self.gran))
        self.dist += int(self.speed * self.gran)

    def crash(self):
        self.crashed = True


class Car(Vehicle):
    length = 15

    def __init__(self, speed, lane):
        super(Car, self).__init__(speed, lane)

    def __str__(self):
        return "*" if self.crashed else ">"

    def __repr__(self):
        return "Car(speed: %s, lane %d, dist: %d" % (self.speed, self.lane, self.dist)


class Truck(Vehicle):
    length = 30

    def __init__(self, speed, lane):
        super(Truck, self).__init__(speed, lane)

    def __str__(self):
        return "*" if self.crashed else "D"

    def __repr__(self):
        return "Truck(speed: %s, lane %d, dist: %d" % (self.speed, self.lane, self.dist)
