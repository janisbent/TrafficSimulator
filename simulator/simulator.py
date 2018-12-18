import time
from .car import Car
from .road import Road
from .speed import MPH, FPS, KPH, MPS


class Simulator:
    def __init__(self, args):
        self.sleep_dur = .25
        self.road = Road(nlanes=3)
        self.ncars = args.ncars
        self.tstep = 0

    def __str__(self):
        return "road"

    def __repr__(self):
        return "Simulator()"

    def setup(self):
        pass

    def reset(self):
        self.tstep = 0

    def print(self):
        print("tstep:", self.tstep)
        print(self.road)
        print()

    def run(self, n=0):
        try:
            if n > 0:
                while self.tstep < n:
                    self.one_step()
                    self.print()
                    time.sleep(self.sleep_dur)
                    self.tstep += 1
            else:
                while True:
                    self.one_step()
                    self.print()
                    time.sleep(self.sleep_dur)
                    self.tstep += 1
        except KeyboardInterrupt:
            i = ""
            while i not in ["c", "q"]:
                i = input("'c' to continue, 'q' to quit, 'h' for help> ")
            if i == "c":
                self.run(n=n)

    def help(self):
        print("Todo...")

    def one_step(self):
        self.road.step()

    def spawn_cars(self):
        pass