# import inputs validator
import inputs

# import functions from other files
import newtons
import gradient


def main():
    # chose method
    chosen_method = int(input(
        'Chose function minimalisation method\n0 - Gradient Descent\n1 - Newtons\nInput: '))

    while chosen_method not in [0, 1]:
        chosen_method = int(input('Insert 0 or 1! Input: '))

    # chose type of func
    chosen_func_type = int(input(
        'Chose function type\n0 - F(x) = ax^3 + bx^2 + cx + d\n1 - G(x) = c + b^Tx + x^TAx\nInput: '))

    while chosen_func_type not in [0, 1]:
        chosen_func_type = int(input('Insert 0 or 1! Input: '))

    # read and validate inputs
    params = inputs.getParams(chosen_func_type)

    if(chosen_func_type == 0):  # Fx
        a = params[0]
        b = params[1]
        c = params[2]
        d = params[3]
    else:  # Gx
        c = params[0]
        b = inputs.getDimentionalVector(params[1])
        A = inputs.getPositiveDefineMatrix(params[1])

    # read and validate input start point
    start_point = inputs.getStartPoint(chosen_func_type, params[1])

    if chosen_method == 0:  # gradient
        if chosen_func_type == 0:  # Fx
            gradient.gradientDescentFx(a, b, c, d, start_point)
        else:  # Gx
            gradient.gradientDescentGx(A, b, c, start_point)
    else:  # newtons
        if chosen_func_type == 0:  # Fx
            newtons.newtonsFx(a, b, c, d, start_point)
        else:  # Gx
            newtons.newtonsGx(A, b, c, start_point)


if __name__ == "__main__":
    main()
