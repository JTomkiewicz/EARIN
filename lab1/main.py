def getParams(funcType):
    if(funcType == 0):
        a, b, c, d = input("Insert parameters: a b c d\nInput: ").split()
        return [a, b, c, d]
    else:
        return 2


def main():
    # chose method
    chosenMethod = int(input(
        "Welcome!\nChose function minimalisation method:\n0 - Gradient Descent\n1 - Newton's\nInput: "))

    if(chosenMethod not in [0, 1]):
        print("Incorrect method!")
        quit()

    # chose type of func
    chosenFuncType = int(input(
        "Chose function type:\n0 - F(x) = ax^3 + bx^2 + cx + d\n1 - G(x) = c + b^Tx + x^TAx\nInput: "))

    if(chosenFuncType not in [0, 1]):
        print("Incorrect function type!")
        quit()

    # get scalar parameters
    params = getParams(chosenFuncType)


if __name__ == "__main__":
    main()
