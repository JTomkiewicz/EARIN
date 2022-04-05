def readInt(msg: str) -> int:
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = int(number)
            break
        except ValueError:
            print('Input must be a int!')

    return int(number)


def clearBoard() -> None:
    global board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]


def printBoard() -> None:
    for i in range(3):
        print(f'|{board[i][0]}|{board[i][1]}|{board[i][2]}|')
    print()


def isPositionValid(position: list) -> bool:
    # check if position is out of range
    if position[0] not in range(3):
        return False
    elif position[1] not in range(3):
        return False
    elif board[position[0]][position[1]] != ' ':  # check if position is not already occupied
        return False

    # position is fine
    return True


def isGameEnded():
    # vertical win
    for i in range(3):
        if board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # horizontal win
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # 1st diagonal win
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # 2nd diagonal win
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            # check if there is still empty space
            if board[i][j] == ' ':
                return None

    # no wins && no empty space => tie
    return ' '


def playGame() -> None:
    global playerTurn

    while True:
        printBoard()
        result = isGameEnded()

        # check if game ended
        if result != None:
            # show result
            if result == 'X' or result == 'O':
                print(f'Game over! {result} win!')
            elif result == ' ':
                print("Game over! It is a tie!")

            # clear board
            clearBoard()
            return

        # player turn
        if playerTurn == 'X':
            while True:

                position = [None, None]

                print('Your turn!')

                # get coordinates from user
                position[0] = readInt('row number')
                position[1] = readInt('column number')

                position[0] -= 1
                position[1] -= 1

                # check if input is valid
                if isPositionValid(position):
                    board[position[0]][position[1]] = 'X'
                    playerTurn = 'O'
                    break
                else:
                    print('Invalid move! Try again.')
        else:  # computer turn
            position = max(-2, 2)[1]
            board[position[0]][position[1]] = 'O'
            playerTurn = 'X'


def max(alpha: int, beta: int) -> tuple:
    maxValue = -2
    maxPosition = [None, None]
    result = isGameEnded()

    if result == 'X':
        return -1, [0, 0]
    elif result == 'O':
        return 1, [0, 0]
    elif result == ' ':
        return 0, [0, 0]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                minValue = min(alpha, beta)[0]

                if minValue > maxValue:
                    maxValue = minValue
                    maxPosition = [i, j]

                board[i][j] = ' '

                # alpha-beta pruning
                if maxValue >= beta:
                    return maxValue, maxPosition
                if maxValue > alpha:
                    alpha = maxValue

    return maxValue, maxPosition


def min(alpha: int, beta: int) -> tuple:
    minValue = 2
    minPosition = [None, None]
    result = isGameEnded()

    if result == 'X':
        return -1, [0, 0]
    elif result == 'O':
        return 1, [0, 0]
    elif result == ' ':
        return 0, [0, 0]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                maxValue = max(alpha, beta)[0]

                if maxValue < minValue:
                    minValue = maxValue
                    minPosition = [i, j]

                board[i][j] = ' '

                # alpha-beta pruning
                if minValue <= alpha:
                    return minValue, minPosition
                if minValue < beta:
                    beta = minValue

    return minValue, minPosition


def main() -> None:
    print('Game begins!\nRows and columns are numerated from 1 to 3\n')
    clearBoard()

    global playerTurn
    playerTurn = 'X'

    playGame()


if __name__ == "__main__":
    main()
