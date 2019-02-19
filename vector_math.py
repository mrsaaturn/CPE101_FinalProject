from data4pt2 import *
from math import *


def scale_vector(vector, scale):
    new_vec = Vector(vector.xdir, vector.ydir, vector.zdir)
    new_vec.xdir = new_vec.xdir * scale
    new_vec.ydir = new_vec.ydir * scale
    new_vec.zdir = new_vec.zdir * scale
    new_vec2 = Vector(new_vec.xdir, new_vec.ydir, new_vec.zdir)
    return new_vec2

def dot_vector(vector1, vector2):
    sum_1 = vector1.xdir * vector2.xdir
    sum_2 = vector1.ydir * vector2.ydir
    sum_3 = vector1.zdir * vector2.zdir
    return sum_1 + sum_2 + sum_3

def length_vector(vector):
    temp= vector.xdir ** 2 + vector.ydir ** 2 + vector.zdir ** 2
    return sqrt (temp)

def normalize_vector (vector):
    length = length_vector(vector)
    new_vec = Vector(vector.xdir, vector.ydir, vector.zdir)
    new_vec.x = new_vec.xdir / length
    new_vec.y = new_vec.ydir / length
    new_vec.z = new_vec.zdir / length
    return new_vec

def difference_point(point1, point2):
    new_point = Point(point1.x, point1.y, point1.z)
    new_point2 = Point(point2.x, point2.y, point2.z)
    new_point.x = new_point.x - new_point2.x
    new_point.y = new_point.y - new_point2.y
    new_point.z = new_point.z - new_point2.z
    new_vec = Vector(new_point.x, new_point.y, new_point.z)
    return new_vec

def difference_vector(vector1, vector2):
    diff_vector = Vector(vector1.xdir, vector1.ydir, vector1.zdir)
    diff_vector2 = Vector(vector2.xdir, vector2.ydir, vector2.zdir)
    diff_vector.xdir = diff_vector.xdir - diff_vector2.xdir
    diff_vector.ydir = diff_vector.ydir - diff_vector2.ydir
    diff_vector.zdir = diff_vector.zdir - diff_vector2.zdir
    return diff_vector

def translate_point(point, vector):
    trans_point = Point(point.x, point.y, point.z)
    trans_point.x = point.x + vector.xdir
    trans_point.y = point.y + vector.ydir
    trans_point.z = point.z + vector.zdir
    return trans_point

def vector_from_to(from_point, to_point):
    point_from = Point(from_point.x, from_point.y, from_point.z)
    point_to = Point(to_point.x, to_point.y, to_point.z)
    vec_from_to = Vector(point_to.x - point_from.x, point_to.y - point_from.y, point_to.z - point_from.z)
    return vec_from_to