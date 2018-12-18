import random
from .car import Car, Truck
from .speed import MPH


class Road:
    def __init__(self, nlanes=1, spawn=0.6, length=100):
        self.lanes = [EdgeLane(length=length, marker="=")]
        for _ in range(nlanes):
            self.lanes += [DrivingLane(spawnr=spawn / nlanes, length=length), DottedLane(length=length)]
        self.lanes.pop()
        self.lanes += [EdgeLane(length=length)]
        # self.lanes = [DrivingLane(spawn=spawn, length=length) for _ in range(nlanes)]
        self.length = length

    def __str__(self):
        return "".join(str(l) for l in self.lanes)

    def step(self):
        for lane in self.lanes:
            lane.step()


class Lane:
    def __init__(self, spawnr, length, marker):
        self.spawnr = spawnr
        self.segments = [Segment(length, marker)]

    def __str__(self):
        return "".join(map(lambda s: str(s), self.segments)) + "\n"

    def __getitem__(self, item):
        return self.segments[0][item]

    def __setitem__(self, key, value):
        self.segments[0][key] = value

    def step(self):
        self.spawn()

    def spawn(self):
        if not self[0] and random.random() < self.spawnr:
            self[0] = Car(MPH(10))


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
    def __init__(self, length, marker):
        self.spots = [None] * length
        self.default = marker

    def __getitem__(self, item):
        return self.spots[item]

    def __setitem__(self, key, value):
        self.spots[key] = value

    def __str__(self):
        ret = "".join(self.default * (len(self.spots) // len(self.default)))
        return "".join(str(d_s[1]) if d_s[1] else d_s[0] for d_s in zip(ret, self.spots))
        # return "".join(map((lambda s: str(s) if s else (self.default len(self.default))), self.spots))

