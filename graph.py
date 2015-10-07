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

    if demand2 == "3":

        from Unit_1 import lesson_3
        print unit1_3
        demand3 = raw_input(query)

        if demand3 == "1":
            lesson_3.get_equation_from_intercepts()
        elif demand3 == "2":
            lesson_2.get_equation_from_points()
        elif demand3 == "3":
            lesson_3.y_intercept_to_parrallel()
        elif demand3 == "4":
            lesson_3.get_perpendicular_bisector_from_points()

    if demand2 == "4":

        print unit1_4

    if demand2 == "5":

        print unit1_5

    if demand2 == "6":

        from Unit_1 import lesson_6
        print unit1_6
        demand3 = raw_input(query)

        if demand3 == "1":
            lesson_6.solve_quadratic()
        if demand3 == "2":
            lesson_6.solve_quadratic_from_factors()
