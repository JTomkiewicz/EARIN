def readInt():
    while True:
        try:
            number = input()
            number = int(number)
            break
        except ValueError:
            print('Input must be a int!')
    return int(number)


def read_params():
    pass
