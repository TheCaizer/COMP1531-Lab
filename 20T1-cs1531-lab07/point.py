from math import sqrt, atan2, cos, sin, isclose, pi

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    @property
    def theta(self):
        return atan2(self.y, self.x)

    @property
    def r(self):
        return sqrt(self.x**2 + self.y**2)

    @r.setter
    def r(self, r):
        self.x = r*cos(self.theta)
        self.y = r*sin(self.theta)

    @theta.setter
    def theta(self, theta):
        prev = self.r
        self.y = self.r*cos(theta)
        self.x = (prev)*sin(theta)


def distance(start, end):
    '''
    Calculate the distance between 2 points.
    '''
    return sqrt((end.x - start.x)**2 + (end.y - start.y**2))

def test_point():
    me = Point(1, 1)
    my_house = Point(2, 1)
    assert isclose(distance(me, my_house), 1, rel_tol=0.01) # Within 1% tolerance
    me.x = 2
    assert isclose(distance(me, my_house), 0, rel_tol=0.01)
    me.y = 0
    assert isclose(me.r, 2, rel_tol=0.01)
    assert isclose(me.theta, 0, rel_tol=0.01)
    me.r = 3
    assert isclose(me.x, 3, rel_tol=0.01)
    me.theta = pi*0.25 # 45 degrees in radians
    assert isclose(me.x, 3*cos(pi*0.25), rel_tol=0.01)
    assert isclose(me.y, 3*cos(pi*0.25), rel_tol=0.01)
