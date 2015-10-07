def get_equation_from_intercepts():
    # get raw input
    x = raw_input("Input X intercept >> ")
    y = raw_input("Input Y intercept >> ")
    # parse raw input
    x1 = float(x)
    y1 = 0
    x2 = 0
    y2 = float(y)
    # get slope
    part1 = y2 - y1
    part2 = x2 - x1
    slope = part1 / part2
    # print out final result
    print "y=" + str(slope) + "x+" + str(y)

def y_intercept_to_parrallel():
    # get raw input
    y_intercept = raw_input("Input desired Y intercept >> ")
    equation1 = raw_input("Input M from form Y = Mx + B >> ")
    # parse input
    slope = float(equation1)
    # get new y-intercept
    print "y=" + str(slope) + "x+" + str(y_intercept)

def get_perpendicular_bisector_from_points():
    # get raw input
    point1 = raw_input("Input X and Y separated by commas in (X,Y) >> ")
    point2 = raw_input("Input X and Y separated by commas in (X,Y) >> ")
    # parse input
    point1 = point1.split(",")
    point2 = point2.split(",")
    x1 = float(point1[0])
    y1 = float(point1[1])
    x2 = float(point2[0])
    y2 = float(point2[1])
    # obtain slope
    part1 = y2 - y1
    part2 = x2 - x1
    slope = part1 / part2
    # get midpoint of Points
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    print str(x_mid)
    print str(y_mid)
    # get reciprocal of slope
    slope = -1 * (1 / slope)
    # plugin point to get y intercept
    mx = slope * x_mid
    if mx == 0:
        b = y_mid
    elif mx != 0:
        b = y_mid / mx
    # print out result
    print "y = " + str(slope) + "x + " + str(b)
