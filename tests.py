from collisionspt2 import *
import unittest
import data4pt2
from vector_math import *
from Castpt2 import *

class TestCases(unittest.TestCase):
    def test_castRay_1(self):
        sphere1 = data4pt2.Sphere(data4pt2.Point(5, 2, 2), 2, (0, 0, 255))
        sphere2 = data4pt2.Sphere(data4pt2.Point(0.5, 1.5, -3.0), 0.5, (255, 0, 0))
        sphere_list = [sphere1, sphere2]
        ray = data4pt2.Ray(data4pt2.Point(6, 3, 2), data4pt2.Vector(7, 0, 5))
        self.assertEquals(cast_ray(sphere_list, ray), Color(0, 0, 255))


    def test_castRay_2(self):
        sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2, (0, 0, 255))
        sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, (255, 0, 0))
        sphere_list = [sphere1, sphere2]
        ray = Ray(Point(6, 3, 2), Vector(1, 1, 1))
        self.assertEquals(cast_ray(sphere_list, ray), Color(255, 255, 255))


if __name__ == '__main__':
   unittest.main()