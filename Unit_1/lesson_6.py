from math import sqrt

def solve_quadratic():
    # get raw input
    equation = raw_input("Input A, B, and C separated with commas from equation Ax^2 + Bx + C = 0 >> ")
    # parse input
    equation = equation.split(",")
    a = float(equation[0])
    b = float(equation[1])
    c = float(equation[2])
    # discriminant of equation
    discriminant = float(( b ** 2 ) - ( 4 * a * c ))
    # try to solve
    try:
        # Hoping for the best
        root1 = (( -1 * b ) + sqrt( discriminant )) / ( 2 * a )
        root2 = (( -1 * b ) - sqrt( discriminant )) / ( 2 * a )
        print "The first root is " + str(root1)
        print "The second root is " + str(root2)
    except ValueError:
        # Case break for imaginary
        print "I'm sorry, your equation involves imaginary numbers.\nWe can't do that yet."

def solve_quadratic_from_factors():
    # get raw input
    factor1 = raw_input("Input A and B separated with commas from first factor ( Ax + B ) >> ")
    factor2 = raw_input("Input A and B separated with commas from second factor ( Ax + B ) >> ")
    # Format user Input
    factor1 = float(factor1.split(","))
    factor2 = float(factor2.split(","))
    x1 = factor1[0]
    b1 = factor1[1]
    x2 = factor2[0]
    b2 = factor2[1]
    
