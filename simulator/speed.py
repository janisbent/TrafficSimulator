
class Speed(float):
    def mph(self): raise NotImplemented

    def fps(self): raise NotImplemented

    def kph(self): raise NotImplemented

    def mps(self): raise NotImplemented


class MPH(Speed):
    def mph(self): return self

    def fps(self): return FPS(self * 1.46667)

    def kph(self): return KPH(self * 1.60934)

    def mps(self): return MPS(self * 0.44704)

    def __str__(self): return "%f mph" % self


class FPS(Speed):
    def mph(self): return MPH(self * 0.681818)

    def fps(self): return self

    def kph(self): return KPH(self * 1.09728)

    def mps(self): return MPS(self * 0.3048)

    def __str__(self): return "%f fps" % self


class KPH(Speed):
    def mph(self): return MPH(self * 0.621371)

    def fps(self): return FPS(self * 0.911344)

    def kph(self): return self

    def mps(self): return MPS(self * 0.277778)

    def __str__(self): return "%f kph" % self


class MPS(Speed):
    def mph(self): return MPH(self * 2.23694)

    def fps(self): return FPS(self * 3.28084)

    def kph(self): return KPH(self * 3.6)

    def mps(self): return self

    def __str__(self): return "%f mps" % self
