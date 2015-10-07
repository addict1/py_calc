from math import sqrt

def get_vertex_full():
    a = float(raw_input("enter a >> "))
    b = float(raw_input("enter b >> "))
    c = float(raw_input("enter c >> "))
    # -b/2a as we all know :)
    vertex_x = (-1*(b))/(2*a)
     # plug it back into the equation
    vertex_y = (((vertex_x**2)*a)+(vertex_x*b)+c)
    # parse results to point
    vertex_full = "(" + str(float(vertex_x)) + "," + str(float(vertex_y)) + ")"
    return vertex_full

def get_zeroes_of_function():
    a = float(raw_input("enter a >> "))
    b = float(raw_input("enter b >> "))
    c = float(raw_input("enter c >> "))

    x_pos = ((-1*b)/(2*a))+(sqrt((b**2)-(4*a*c))/(2*a))
    x_neg = ((-1*b)/(2*a))-(sqrt((b**2)-(4*a*c))/(2*a))
    print str(x_pos) + " " + str(x_neg)
