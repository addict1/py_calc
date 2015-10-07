print """[1] Unit 1
[2] Unit 2
[3] Unit 3
"""
demand1 = raw_input("Pick number >> ")

if demand1 == "1":
    print """[1] Lesson 1
[2] Lesson 2"""
    demand2 = raw_input("Pick number >> ")

    if demand2 == "1":
        print """[1] Get Midpoint from Equation
[2] Get Midpoint from Points
[3] Solve Systems of Equations
[4] Get Equation from Points
"""
        demand3 = raw_input("Pick number >> ")
        if demand3 == "1":
            from Unit_1 import lesson_1
            lesson_1.get_equation_from_points()
