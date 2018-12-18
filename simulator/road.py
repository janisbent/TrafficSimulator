

class Road:
    def __init__(self, nlanes=1, spawn=1.0, length=100):
        self.lanes = [Lane(spawn=spawn, length=length) for _ in range(nlanes)]
        self.length = length

    def __str__(self):
        buf = "=" * self.length + "\n"
        top = True
        for l in self.lanes:
            if not top:
                buf += "- " * (self.length // 2) + "\n"
            else:
                top = False
            buf += str(l) + "\n"
        buf += "-" * self.length + "\n"
        return buf


class Lane:
    def __init__(self, spawn=1.0, length=10):
        self.spawn = spawn
        self.segments = [Segment(length)]

    def __str__(self):
        return "".join(map(lambda s: str(s), self.segments))


class Segment:
    def __init__(self, length):
        self.spots = [None] * length

    def __getitem__(self, dist):
        return self.spots[dist]

    def __str__(self):
        return "".join(map((lambda s: str(s) if s else " "), self.spots))

