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
"""
        demand3 = raw_input("Pick number >> ")
        from Unit_1 import lesson_1
        if demand3 == "1":
            lesson_1.get_midpoint()
        elif demand3 == '2':
            lesson_1.solve_sys_of_equations()
    if demmand2 == "2":
        print """[1] Get Equation of Line from Points
[2] Check for Parrallel
[3] Check for Perpendicular"""
        from Unit_1 import lesson_2
        demand3 = raw_input("Pick number >> ")
        if demmand3 == "1":
            lesson_2.get_equation_from_points()
        if demmand3 == "2":
            lesson_2.check_for_par()
