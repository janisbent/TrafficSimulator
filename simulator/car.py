


class Car:
    length = 5

    def __init__(self, speed):
        self.speed = speed
        self.crashed = False

    def __str__(self):
        return "*" if self.crashed else ">"
