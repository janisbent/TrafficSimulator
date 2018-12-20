import random
from .car import Car, Truck
from .speed import MPH
from .situation import Situation


# TODO: docstring
class Road:
    def __init__(self, nlanes=1, spawn=0.6, length=100):
        self.lanes = [EdgeLane(length=length, marker="=")]
        for _ in range(nlanes):
            self.lanes += [DrivingLane(spawnr=spawn / nlanes, length=length), DottedLane(length=length)]
        self.lanes.pop()
        self.lanes += [EdgeLane(length=length)]
        self.length = length

    def __str__(self):
        return "".join(str(l) for l in self.lanes)

    def __getitem__(self, item):
        return self.lanes[item]

    def __setitem__(self, key, value):
        self.lanes[key] = value

    def step(self):
        # print("****")
        for lane in self.lanes:
            lane.step()
        # print("****"*2)

# TODO: Cars should be stored in Road, not Lane
# TODO: Segments should probably have lanes, not vice versa


class Lane:
    def __init__(self, spawnr, length, marker):
        self.spawnr = spawnr
        self.segments = [Segment(0, length, marker)]

    def __str__(self):
        return "".join(map(lambda s: str(s), self.segments)) + "\n"

    def __getitem__(self, item):
        return self.segments[0][item]

    def __setitem__(self, key, value):
        self.segments[0][key] = value

    def step(self):
        self.spawn()
        for s in self.segments:
            s.stepall()

    def spawn(self):
        if not self[0] and random.random() < self.spawnr:
            self.segments[0].add_car()


class DrivingLane(Lane):
    def __init__(self, spawnr=1.0, length=10):
        super(DrivingLane, self).__init__(spawnr, length, " ")
        self.drivable = True


class EdgeLane(Lane):
    def __init__(self, spawnr=0, length=10, marker="-"):
        super(EdgeLane, self).__init__(spawnr, length, marker)
        self.drivable = False
        self.marker = marker


class DottedLane(Lane):
    def __init__(self, spawnr=0, length=10):
        super(DottedLane, self).__init__(spawnr, length, "- ")
        self.drivable = False


class Segment:
    def __init__(self, start, length, marker, speedl=MPH(10)):
        self.start = start
        self.length = length
        self.cars = []
        self.road = [None] * length * Car.length
        self.spots = [None] * length
        self.default = marker
        self.speedl = speedl

    def __getitem__(self, item):
        return self.spots[item - self.start]

    def __setitem__(self, key, value):
        self.spots[key - self.start] = value

    def __str__(self):
        self.refresh()
        ret = "".join(self.default * (len(self.spots) // len(self.default)))
        return "".join(str(d_s[1]) if d_s[1] else d_s[0] for d_s in zip(ret, self.spots))

    def __len__(self):
        return self.length

    def refresh(self):
        self.road = [None] * self.length * Car.length  # TODO: default road instead of None
        self.spots = [None] * self.length
        for c in self.cars:
            start = c.pos - self.start

            for i in range(start, start + Car.length):  # TODO: catch out of bounds cars
                if self.road[i]:
                    self.road[i].crash()
                    c.crash()
                else:
                    self.road[i] = c
            self.spots[c.pos // Car.length] = c

    def add_car(self, car=None):
        if car:
            self.cars += car
        else:
            self.cars.append(Car(MPH(self.speedl)))

    def stepall(self):
        for c in self.cars:
            c.drive(Situation())  # TODO: Update Situation
        self.refresh()  # TODO: Figure out how to hand off cars between segments

