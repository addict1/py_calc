from ul import *

print units
demand1 = raw_input(query)

if demand1 == "1":

    print unit1
    demand2 = raw_input(query)

    if demand2 == "1":

        from Unit_1 import lesson_1
        print unit1_1
        demand3 = raw_input(query)

        if demand3 == "1":
            lesson_1.get_midpoint()
        elif demand3 == '2':
            lesson_1.solve_sys_of_equations()

    if demand2 == "2":

        from Unit_1 import lesson_2
        print unit1_2
        demand3 = raw_input(query)

        if demand3 == "1":
            lesson_2.get_equation_from_points()
        elif demand3 == "2":
            lesson_2.check_for_pro()

    if demmand2 == "3":

        from Unit_1 import lesson_3
        print unit1_3
        demmand3 = raw_input(query)

        if demmand3 == "1":
            lesson_3.get_equation_from_intercepts()
        elif demmand3 == "2":
            lesson_2.get_equation_from_points()
        elif demmand3 == "3":
            lesson_3.y_intercept_to_parrallel()
        elif demmand3 == "4":
            lesson_3.get_perpendicular_bisector_from_points()
