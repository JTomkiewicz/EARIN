def read_int():
    while True:
        try:
            number = input()
            number = int(number)
            break
        except ValueError:
            print('Input must be a integer!')
    return int(number)


def read_params():
    print('STEP 1: Enter the evidence:')
    evidence = input()

    print('STEP 2: Enter the query:')
    query = input()

    print('STEP 3: Enter the number of steps:')
    nr_steps = read_int()

    return evidence, query, nr_steps
