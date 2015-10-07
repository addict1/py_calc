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
    equation1 = raw_input("Input A, B, and C separated by commas in Ax + By + C >> ")
    print "Second Equation"
    equation2 = raw_input("Input A, B, and C separated by commas in Ax + By + C >> ")
    # organize info
    equation1 = equation1.split(',')
    equation2 = equation2.split(',')
    # assign independent variables
    x1 = float(equation1[0])
    x2 = float(equation2[0])
    y1 = float(equation1[1])
    y2 = float(equation2[1])
    c1 = float(equation1[2])
    c2 = float(equation2[2])
    # get determinant
    det1 = x1 * y2
    det2 = ( -1 * x2 ) * ( -1 * y1 )
    det1_2 = det1 - det2
    determinant = 1 / det1_2
    # multiply matrix
    x1 = determinant * x1
    x2 = determinant * x2
    y1 = determinant * y1
    y2 = determinant * y2
    # multiply matrix of c's and ab matrix
    term1 = ( y2 * c1 ) + ( ( -1 * y1 ) * c2 )
    term2 = ( ( -1 * x2 ) * c1 ) + ( x1 * c2 )
    print "(" + str(term1) + "," + str(term2) + ")"

def get_equation_from_points():
    # get info
    point1 = raw_input("Input X and Y separated by commas in (X,Y) >> ")
    point2 = raw_input("Input X and Y separated by commas in (X,Y) >> ")
    # organize info
    point1 = point1.split(",")
    point2 = point2.split(",")
    x1 = float(point1[0])
    y1 = float(point1[1])
    x2 = float(point2[0])
    y2 = float(point2[1])
    # get slope
    part1 = y2 - y1
    part2 = x2 - x1
    slope = part1 / part2
    # get y-intercept
    mx = slope * x1
    if mx == 0:
        b = y1
    elif mx != 0:
        b = y1 / mx
    # print out final results
    print "y = " + str(slope) + "x + " + str(b)
