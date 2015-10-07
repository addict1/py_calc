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

def check_for_par():
    # get info
    #equation1 = raw_input()

def check_for_per():
    pass
