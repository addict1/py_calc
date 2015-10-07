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
[2] Solve Systems of Equations
[3] Get Equation from Points
"""
        demand3 = raw_input("Pick number >> ")
        from Unit_1 import lesson_1
        if demand3 == "1":
            lesson_1.get_midpoint()
        elif demand3 == '2':
            lesson1.solve_sys_of_equations()
        elif demand3 == '3':
            lesson1.get_equation_from_points()
