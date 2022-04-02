def readInt(msg: str):
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = int(number)
            break
        except ValueError:
            print('Input must be a int!')

    return int(number)


def clearBoard():
    global board
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]


def printBoard():
    for i in range(3):
        print(f'|{board[i][0]}|{board[i][1]}|{board[i][2]}|')
    print()


def isValid(position):
    # check if position is out of range or position is occupied
    if position[0] not in range(3):
        return False
    elif position[1] not in range(3):
        return False
    elif board[position[0]][position[1]] != '.':
        return False

    # position is valid
    return True


def isEnd():
    # vertical win
    for i in range(3):
        if board[0][i] != '.' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # horizontal win
    for i in range(3):
        if board[i][0] != '.' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # first diagonal win
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # second diagonal win
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # check if board is fully occupied
    for i in range(3):
        for j in range(3):
            # check if there is still empty space
            if board[i][j] == '.':
                return None

    # tie
    return '.'


def game():
    global playerTurn

    while True:
        printBoard()
        result = isEnd()

        # check if game ended
        if result != None:
            if result == 'X' or result == 'O':
                print(f'Game over! {result} win!')
            elif result == '.':
                print("Game over! It is a tie!")

            clearBoard()
            return

        # player turn
        if playerTurn == 'X':
            while True:

                position = [None, None]
                position = min(-2, 2)[1]

                print(
                    f'Algorithm recomends to place X at row = {position[0]} and column = {position[1]}')

                # get coordinates from user
                position[0] = readInt('row number')
                position[1] = readInt('column number')

                # check if input is valid
                if isValid(position):
                    board[position[0]][position[1]] = 'X'
                    playerTurn = 'O'
                    break
                else:
                    print('Invalid move! Try again.')

        else:
            position = max(-2, 2)[1]
            board[position[0]][position[1]] = 'O'
            playerTurn = 'X'


def max(alpha: int, beta: int):
    maxValue = -2
    maxPosition = [None, None]
    result = isEnd()

    if result == 'X':
        return (-1, [0, 0])
    elif result == 'O':
        return (1, [0, 0])
    elif result == '.':
        return (0, [0, 0])

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                minValue = min(alpha, beta)[0]

                if minValue > maxValue:
                    maxValue = minValue
                    maxPosition = [i, j]

                board[i][j] = '.'

                # alpha-beta pruning
                if maxValue >= beta:
                    return (maxValue, maxPosition)
                if maxValue > alpha:
                    alpha = maxValue

    return (maxValue, maxPosition)


def min(alpha: int, beta: int):
    minValue = 2
    minPosition = [None, None]
    result = isEnd()

    if result == 'X':
        return (-1, [0, 0])
    elif result == 'O':
        return (1, [0, 0])
    elif result == '.':
        return (0, [0, 0])

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                maxValue = max(alpha, beta)[0]

                if maxValue < minValue:
                    minValue = maxValue
                    minPosition = [i, j]

                board[i][j] = '.'

                # alpha-beta pruning
                if minValue <= alpha:
                    return (minValue, minPosition)
                if minValue < beta:
                    beta = minValue

    return (minValue, minPosition)


def main():
    clearBoard()

    global playerTurn
    playerTurn = 'X'

    game()


if __name__ == "__main__":
    main()
