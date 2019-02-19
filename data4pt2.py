from utility import *
class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        xeq = epsilon_equal(self.x, other.x)
        yeq = epsilon_equal(self.y, other.y)
        zeq = epsilon_equal(self.z, other.z)
        return xeq and yeq and zeq


class Vector():
    def __init__(self, xdir, ydir, zdir):
        self.xdir = xdir
        self.ydir = ydir
        self.zdir = zdir
    def __eq__(self, other):
        xdireq = epsilon_equal(self.xdir, other.xdir)
        ydireq = epsilon_equal(self.ydir, other.ydir)
        zdireq = epsilon_equal(self.zdir, other.zdir)
        return xdireq and ydireq and zdireq


class Ray():
    """this represents the starting point displaced by the vector object"""

    def __init__(self, pt, dir):
        """ Parameters are the pt = point object, dir = vector object"""
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pteq = self.pt == other.pt
        direq = self.dir == other.dir
        return pteq and direq



class Color():
    def __init__ (self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


    def __eq__(self, other):
        req = epsilon_equal(self.r, other.r)
        geq = epsilon_equal(self.g, other.g)
        beq = epsilon_equal(self.b, other.b)
        return req and geq and beq


class Sphere():
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = Color(color[0], color[1], color[2])

    def __eq__(self, other):
        centereq = self.center == other.center
        radiuseq = self.radius == other.radius
        coloreq = self.color == other.color
        return centereq and radiuseq and coloreq


