import sys
import data4pt2
from Castpt2 import *
w = 512
h = 384
print "P3 "
print "512 384 "
print "255"
#print str(w) + ' ' + str(h)


eye_point = data4pt2.Point(0.0, 0.0, -14.0)
sphere1 = data4pt2.Sphere(data4pt2.Point(1.0, 1.0, 0.0), 2, (0, 0, 255))
sphere2 = data4pt2.Sphere(data4pt2.Point(0.5, 1.5, -3.0), 0.5, (255, 0, 0))
sphere_list = [sphere1, sphere2]
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5



cast_all_rays(min_x, max_x, min_y, max_y, w, h, eye_point, sphere_list)




