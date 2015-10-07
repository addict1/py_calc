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
    pass
