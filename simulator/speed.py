

# TODO: docstrings
class Speed(float):
    def mph(self): raise NotImplemented

    def fps(self): raise NotImplemented

    def kph(self): raise NotImplemented

    def mps(self): raise NotImplemented

    def __int__(self): return super(Speed, self).__int__()


def asmph(func):
    def tomph(self, s):
        try:
            return func(self, s.mph())
        except AttributeError:
            return func(self, s)
    return tomph


def asfps(func):
    def tomph(self, s):
        try:
            return func(self, s.fps())
        except AttributeError:
            return func(self, s)
    return tomph


def askph(func):
    def tomph(self, s):
        try:
            return func(self, s.kph())
        except AttributeError:
            return func(self, s)
    return tomph


def asmps(func):
    def tomph(self, s):
        try:
            return func(self, s.mps())
        except AttributeError:
            return func(self, s)
    return tomph


class MPH(Speed):
    def mph(self): return self

    def fps(self): return FPS(self * 1.46667)

    def kph(self): return KPH(self * 1.60934)

    def mps(self): return MPS(self * 0.44704)

    def __str__(self): return "%.1f mph" % self

    def __repr__(self): return "%.1f mph" % self

    @asmph
    def __add__(self, other): return MPH(float.__add__(self, other))

    @asmph
    def __radd__(self, other): return MPH(float.__radd__(self, other))

    @asmph
    def __mul__(self, other): return MPH(float.__mul__(self, other))

    @asmph
    def __rmul__(self, other): return MPH(float.__rmul__(self, other))

    @asmph
    def __sub__(self, other): return MPH(float.__sub__(self, other))

    @asmph
    def __rsub__(self, other): return MPH(float.__rsub__(self, other))

    @asmph
    def __truediv__(self, other): return MPH(float.__truediv__(self, other))

    @asmph
    def __rtruediv__(self, other): return MPH(float.__rtruediv__(self, other))


class FPS(Speed):
    def mph(self): return MPH(self * 0.681818)

    def fps(self): return self

    def kph(self): return KPH(self * 1.09728)

    def mps(self): return MPS(self * 0.3048)

    def __str__(self): return "%.1f fps" % self

    def __repr__(self): return "%.1f fps" % self

    @asfps
    def __add__(self, other): return FPS(float.__add__(self, other))

    @asfps
    def __radd__(self, other): return FPS(float.__radd__(self, other))

    @asfps
    def __mul__(self, other): return FPS(float.__mul__(self, other))

    @asfps
    def __rmul__(self, other): return FPS(float.__rmul__(self, other))

    @asfps
    def __sub__(self, other): return FPS(float.__sub__(self, other))

    @asfps
    def __rsub__(self, other): return FPS(float.__rsub__(self, other))

    @asfps
    def __truediv__(self, other): return FPS(float.__truediv__(self, other))

    @asfps
    def __rtruediv__(self, other): return FPS(float.__rtruediv__(self, other))


class KPH(Speed):
    def mph(self): return MPH(self * 0.621371)

    def fps(self): return FPS(self * 0.911344)

    def kph(self): return self

    def mps(self): return MPS(self * 0.277778)

    def __str__(self): return "%.1f kph" % self

    def __repr__(self): return "%.1f kph" % self

    @askph
    def __add__(self, other): return KPH(float.__add__(self, other))

    @askph
    def __radd__(self, other): return KPH(float.__radd__(self, other))

    @askph
    def __mul__(self, other): return KPH(float.__mul__(self, other))

    @askph
    def __rmul__(self, other): return KPH(float.__rmul__(self, other))

    @askph
    def __sub__(self, other): return KPH(float.__sub__(self, other))

    @askph
    def __rsub__(self, other): return KPH(float.__rsub__(self, other))

    @askph
    def __truediv__(self, other): return KPH(float.__truediv__(self, other))

    @askph
    def __rtruediv__(self, other): return KPH(float.__rtruediv__(self, other))


class MPS(Speed):
    def mph(self): return MPH(self * 2.23694)

    def fps(self): return FPS(self * 3.28084)

    def kph(self): return KPH(self * 3.6)

    def mps(self): return self

    def __str__(self): return "%.1f mps" % self

    def __repr__(self): return "%.1f mps" % self

    @asmps
    def __add__(self, other): return MPS(float.__add__(self, other))

    @asmps
    def __radd__(self, other): return MPS(float.__radd__(self, other))

    @asmps
    def __mul__(self, other): return MPS(float.__mul__(self, other))

    @asmps
    def __rmul__(self, other): return MPS(float.__rmul__(self, other))

    @asmps
    def __sub__(self, other): return MPS(float.__sub__(self, other))

    @asmps
    def __rsub__(self, other): return MPS(float.__rsub__(self, other))

    @asmps
    def __truediv__(self, other): return MPS(float.__truediv__(self, other))

    @asmps
    def __rtruediv__(self, other): return MPS(float.__rtruediv__(self, other))
