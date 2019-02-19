from data4pt2 import *
from vector_math import *
import math


def discriminant (b, a, c):
	#Returns the discriminant
	return b**2 - 4*a*c


def quadratic_formula ( discr, b, a):
	# returns a list of real roots, solves for t
    if discr >= 0:
        return [(-b + math.sqrt(discr)) / (2*a), (-b - math.sqrt(discr))/(2*a)]
    else:
        return None


def finding_coefficients(ray, sphere):
    a = dot_vector(ray.dir, ray.dir)
    b_1 = difference_point(ray.pt , sphere.center)
    b_2 = scale_vector(b_1, 2)
    b = dot_vector(b_2, ray.dir)
    c_1 = dot_vector(b_1,b_1)
    c = (c_1 - sphere.radius**2)
    return [a,b,c]


def sphere_intersection_point(ray, sphere):
    result = finding_coefficients(ray, sphere)
    a = result[0]
    b = result[1]
    c = result[2]
    discr = discriminant(b,a,c)
    roots= quadratic_formula(discr, b, a)

    if discr >= 0:
        roots = quadratic_formula(discr, b, a)
        if roots == None:
            return None
        if roots[0] >= 0 and roots[1] >= 0:
            if roots[0] > roots[1]:
                return translate_point(ray.pt, scale_vector(ray.dir, roots[1]))
            else:
                return translate_point(ray.pt, scale_vector(ray.dir, roots[0]))
        elif roots[0] < 0 and roots[1] < 0:
            return None
        if roots[0] >= 0 and roots[1] < 0:
            return translate_point(ray.pt, scale_vector(ray.dir, roots[0]))
        if roots[1] >= 0 and roots[0] < 0:
            return translate_point(ray.pt, scale_vector(ray.dir, roots[1]))

    #convert t back to point- -might be weird with the plus t, might need to do scalars and things to actually *add* things


def tTuPoint( t, ray):
    # adding a point to a vector is translating the point
    pointt = translate_point(ray.pt, scale_vector(ray.dir, t))
    return pointt


def find_intersection_points(sphere_list, ray):
    newlist = []
    for special_boy_sphere in sphere_list:
        why = sphere_intersection_point(ray, special_boy_sphere)
        if why is not None:
            newlist.append((special_boy_sphere, why))
    return newlist


def sphere_normal_at_point(sphere,point):
    # do vector from the origin to the point and then have it have a magnitude of 1
    norm_dir = vector_from_to(sphere.center, point)
    return normalize_vector(norm_dir)