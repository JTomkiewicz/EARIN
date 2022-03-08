import numpy as np
import time

# import inputs validator
import inputs

# import functions from other files
import newtons
import gradient


def main():
    # chose method
    chosen_method = 2
    print('Chose function minimalisation method\n0 - Gradient Descent\n1 - Newtons')
    while True:
        chosen_method = inputs.readScalar('method ID')
        if (chosen_method in [0, 1]):
            break
        print('Insert 0 or 1!')

    # chose type of func
    chosen_func_type = 2
    print('Chose function type\n0 - F(x) = ax^3 + bx^2 + cx + d\n1 - G(x) = c + b^Tx + x^TAx')
    while True:
        chosen_func_type = inputs.readScalar('function ID')
        if (chosen_func_type in [0, 1]):
            break
        print('Insert 0 or 1!')

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

    print('Would you like to use batch mode?\n0 - No\n1 - Yes')
    while True:
        batch_mode = inputs.readScalar('batch mode ID')
        if (batch_mode in [0, 1]):
            break
        print('Insert 0 or 1!')

    if batch_mode == 0:
        n = 1  # when batch mode not selected, perform only 1 iteration
    else:
        # how many times run
        print('How many times run program?')
        n = inputs.readScalar('n')
        n = int(n)

    # placeholder for results
    result_x = []
    result_func_x = []

    start_global_time = time.time()

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

    print('\nNr of seconds: ' + str(time.time() - start_global_time))

    if batch_mode == 0:
        print('\nFound x:\n' + str(result_x[0]))
        print('F(x):' if chosen_func_type == 0 else 'G(x):')
        print(str(result_func_x[0]))
    else:
        print('\nFunctions were performed ' + str(n) + ' times\n')

        if chosen_func_type == 0:  # Fx
            # mean values
            print('Mean value of x:\n' +
                  str(np.mean(np.array(result_x), dtype=np.float64)))

            print('Mean value of F(x):\n' +
                  str(np.mean(np.array(result_func_x), dtype=np.float64)))

            # standard deviations
            print('Standard deviation of x:\n' +
                  str(np.std(np.array(result_x))))

            print('Standard deviation of F(x):\n' +
                  str(np.std(np.array(result_func_x))))

        else:  # Gx
            # mean values
            mean_result = np.zeros((params[1], 1))
            for matrix in result_x:
                mean_result = np.add(mean_result, matrix)

            mean_result = mean_result / n

            print('Mean value of x:\n' + str(mean_result))

            print('Mean value of G(x):\n' +
                  str(np.mean(np.array(result_func_x))))

            # standard deviations
            deviation = np.zeros((params[1], 1))
            for matrix in result_x:
                substract = np.subtract(matrix, mean_result)
                deviation = np.add(deviation, np.square(substract))
            deviation = deviation / n
            print('Standard deviation of x:\n' + str(deviation))

            print('Standard deviation of G(x):\n' +
                  str(np.std(np.array(result_func_x))))


if __name__ == "__main__":
    main()
