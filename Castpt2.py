from collisionspt2 import *
from data4pt2 import *
from vector_math import *

'''In cast.py, update the cast_ray function to return the color of the sphere with the nearest intersection point 
(to the ray's origin), if there is an intersection, or a default color of white (1.0, 1.0, 1.0) if there is no intersection. 
Note: Do not make any assumptions about the order of the spheres in the array as relates to the nearness of the spheres.'''

def distance(pt1, pt2):
    # distance = sqrt (x2-x1)^2 + (y2-y1)^2
    x_dist = (pt2.x - pt1.x) ** 2
    y_dist = (pt2.y - pt1.y) ** 2
    dist = math.sqrt(x_dist + y_dist)
    return dist


def distanceEye(eye_point, sphere):
    dist = distance(eye_point, sphere.center)
    return dist


def cast_ray(sphere_list, ray):
# Returns color if you have an intersection
    intersections = find_intersection_points(sphere_list, ray)
    if len(intersections) > 0:
        distances = []
        for inter in intersections:
            distances.append(distance(ray.pt, inter[1]))
        indexOfClosest = distances.index(min(distances))
        return Color(intersections[indexOfClosest][0].color.r, intersections[indexOfClosest][0].color.g, intersections[indexOfClosest][0].color.b)
    else:
        return Color(255, 255, 255)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
# calls the cast_ray for however many pixels we have
# gonna need a nested for loop to do each row of pixels
# inner loop does each pixel, outer does each row
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
# nest loops, process all rays
    counter_y = 0
    h = max_y
    while counter_y < height:
        counter_x = 0
        w = min_x
        while counter_x < width:
            z = 0
            magicVector = vector_from_to(eye_point, Point(w, h, 0))
            lesBeam = Ray(eye_point, magicVector)
            if cast_ray(sphere_list, lesBeam) != Color(255, 255, 255):
                print cast_ray(sphere_list, lesBeam).r, cast_ray(sphere_list, lesBeam).g, cast_ray(sphere_list, lesBeam).b
            else:
                print 255, 255, 255
            w += delta_x
            counter_x += 1
        counter_y +=1
        h -= delta_y


'''
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
# nest loops, process all rays
    counter_y = 0
    h = max_y
    whiteColor = Color(255, 255, 255)
    while counter_y < height:
        counter_x = 0
        w = min_x
        while counter_x < width:
            z = 0
            magicVector = vector_from_to(eye_point, Point(w, h, 0))
            lesBeam = Ray(eye_point, magicVector)
            gay = cast_ray(sphere_list, lesBeam)
            if gay != whiteColor:
                print gay.r, gay.g, gay.b
            else:
                print whiteColor.r, whiteColor.g, whiteColor.b
                w += delta_x
            counter_x += 1
        counter_y +=1
        h -= delta_y
'''




