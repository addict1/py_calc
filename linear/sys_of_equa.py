
def solve_for_x_y():

    equation1 = raw_input("Input 1st equation >> ")
    equation2 = raw_input("Input 2nd equation >> ")
    equation3 = raw_input("Input 3rd equation >> ")

    if equation3 == '':
        solve_2()
    elif equation3 != '':
        solve_3()
