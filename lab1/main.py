import numpy as np

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

    # ask user for batch mode
    batch_mode = int(
        input('Would you like to use batch mode?\n0 - No\n1 - Yes\nInput: '))

    while batch_mode not in [0, 1]:
        batch_mode = int(input('Insert 0 or 1! Input: '))

    if batch_mode == 0:
        n = 1  # when batch mode not selected, perform only 1 iteration
    else:
        while True:
            try:  # how many times run
                n = input('How many times run program?\nInput: ')
                n = int(n)
                break
            except ValueError:
                print('Input must be a int! Input: ')

    # placeholder for results
    result_x = []
    result_func_x = []

    for i in range(n):  # perform n loops
        if chosen_method == 0:  # gradient
            if chosen_func_type == 0:  # Fx
                result = gradient.gradientDescentFx(a, b, c, d, start_point)
            else:  # Gx
                result = gradient.gradientDescentGx(A, b, c, start_point)

        else:  # newtons
            if chosen_func_type == 0:  # Fx
                result = newtons.newtonsFx(a, b, c, d, start_point)
            else:  # Gx
                result = newtons.newtonsGx(A, b, c, start_point)

        result_x.append(result[0])
        result_func_x.append(result[1])

    if batch_mode == 0:
        print('Found x:\n' + str(result_x[0]))
        print('F(x):' if chosen_func_type == 0 else 'G(x):')
        print(str(result_func_x[0]))
    else:
        print('Functions were performed ' + str(n) + ' times')

        if chosen_func_type == 0:
            # mean values
            print('Mean value of x:\n' + str(np.mean(np.array(result_x))))

            print('Mean value of F(x):\n' +
                  str(np.mean(np.array(result_func_x))))

            # standard deviations
            print('Standard deviation of x:\n' +
                  str(np.std(np.array(result_x))))

            print('Standard deviation of F(x):\n' +
                  str(np.std(np.array(result_func_x))))


if __name__ == "__main__":
    main()
