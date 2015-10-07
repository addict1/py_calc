from equation import get_two_points
from math import sqrt

def get_midpoint():
    x1 = float(raw_input("X of first point >> "))
    y1 = float(raw_input("Y of first point >> "))
    x2 = float(raw_input("X of second point >> "))
    y2 = float(raw_input("Y of second point >> "))
    mid1 = (x2 - x1)**2
    mid2 = (y2 - y1)**2
    midpoint = sqrt(mid1 + mid2)
    print midpoint

def solve_sys_of_equations():
    # get info
    print "First Equation : "
    equation1 = raw_input("Input A, B, and C separated by commas Ax + By + C >> ")
    print "Second Equation"
    equation2 = raw_input("Input A, B, and C separated by commas Ax + By + C >> ")
    # organize info
    equation1 = equation1.split(',')
    equation2 = equation2.split(',')
