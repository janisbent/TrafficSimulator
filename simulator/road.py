import random
from .car import Car, Truck
from .speed import MPH
from .situation import Situation


# TODO: docstring
class Road:
    def __init__(self, nlanes=1, spawn=0.6, length=10):
        self.lanes = [EdgeLane(0, length=length, marker="=")]
        for _ in range(nlanes):
            self.lanes += [DrivingLane(len(self.lanes), spawnr=spawn / nlanes, length=length),
                           DottedLane(len(self.lanes) + 1, length=length)]
        self.lanes.pop()
        self.lanes += [EdgeLane(len(self.lanes) + 1, length=length)]
        self.length = length
        self.cars = []

    def __str__(self):
        self.refresh()
        return "".join(str(l) for l in self.lanes)

    def __getitem__(self, item):
        return self.lanes[item]

    def __setitem__(self, key, value):
        self.lanes[key] = value

    def step(self):
        for l in self.lanes:
            c = l.spawn()
            if c:
                self.cars.append(c)
        for c in self.cars:
            c.drive(Situation())  # TODO: Update Situation

    def refresh(self):
        for l in self.lanes:
            l.clear()
        for c in self.cars:
            try:
                for i in range(c.dist, c.dist + Car.length):
                    if self[c.lane][i]:
                        self[c.lane][i].crash()
                        c.crash()
                    else:
                        self[c.lane][i] = c
            except IndexError:
                self.cars.remove(c)
                self.refresh()
                break

# TODO: Cars should be stored in Road, not Lane


class Lane:
    def __init__(self, laneno, spawnr, length, marker):
        self.laneno = laneno
        self.spawnr = spawnr
        self.segments = [Segment(0, length, marker)]

    def __str__(self):
        return "".join(map(lambda s: str(s), self.segments)) + "\n"

    def __getitem__(self, item):
        return self.segments[0][item]

    def __setitem__(self, key, value):
        self.segments[0][key] = value

    def spawn(self):
        if not self[Car.length - 1] and random.random() < self.spawnr:
            return Car(MPH(self.segments[0].speedl), self.laneno)

    def clear(self):
        for s in self.segments:
            s.clear()


class DrivingLane(Lane):
    def __init__(self, laneno, spawnr=1.0, length=10):
        super(DrivingLane, self).__init__(laneno, spawnr, length, " ")
        self.drivable = True


class EdgeLane(Lane):
    def __init__(self, laneno, spawnr=0, length=10, marker="-"):
        super(EdgeLane, self).__init__(laneno, spawnr, length, marker)
        self.drivable = False
        self.marker = marker


class DottedLane(Lane):
    def __init__(self, laneno, spawnr=0, length=10):
        super(DottedLane, self).__init__(laneno, spawnr, length, "- ")
        self.drivable = False


class Segment:
    def __init__(self, start, length, marker, speedl=MPH(10)):
        self.start = start
        self.length = length
        self.road = [None] * length * Car.length
        self.spots = [None] * length
        self.default = marker
        self.speedl = speedl

    def __getitem__(self, item):
        return self.road[item - self.start]

    def __setitem__(self, key, car):
        self.road[key - self.start] = car
        if car:
            self.spots[car.dist // Car.length] = car

    def __str__(self):
        ret = "".join(self.default * (len(self.spots) // len(self.default)))
        return "".join(str(d_s[1]) if d_s[1] else d_s[0] for d_s in zip(ret, self.spots))

    def __len__(self):
        return self.length

    def clear(self):
        self.road = [None] * self.length * Car.length  # TODO: default road instead of None
        self.spots = [None] * self.length


