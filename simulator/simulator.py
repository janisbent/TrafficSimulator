import time
from .road import Road


class Simulator:
    def __init__(self, args):
        self.sleep_dur = .1
        self.road = Road(nlanes=3, spawn=.05)
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
            else:
                while True:
                    self.one_step()
                    self.print()
                    time.sleep(self.sleep_dur)
        except KeyboardInterrupt:
            i = ""
            while i not in ["c", "q"]:
                i = input("'c' to continue, 'q' to quit, 's' for one step, 'h' for help> ")
                if i == "s":
                    self.one_step()
            if i == "c":
                self.run(n=n)

    def help(self):
        print("Todo...")

    def one_step(self):
        self.tstep += 1
        self.road.step()

    def spawn_cars(self):
        pass
