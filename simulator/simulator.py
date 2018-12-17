import time
from .car import Car
from .road import Road
from .speed import MPH, FPS, KPH, MPS


class Simulator:
    def __init__(self, args):
        self.sleep_dur = .1
        self.road = Road()
        self.ncars = args.ncars

    def __str__(self):
        return "road"

    def __repr__(self):
        return "Simulator()"

    def setup(self):
        pass

    def reset(self):
        pass

    def print(self):
        pass

    def run(self, n=0):
        if n > 0:
            for _ in range(n):
                self.one_step()
                self.print()
                time.sleep(self.sleep_dur)
        else:
            while True:
                self.one_step()
                self.print()
                time.sleep(self.sleep_dur)

    def one_step(self):
        pass

    def spawn_cars(self):
        pass