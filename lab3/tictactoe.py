import time


def clearBoard():
    global board
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]


def printBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            print('{}|'.format(board[i][j]), end=" ")
        print()
    print()


def isValid(position):
    if position[0] < 0 or position[0] > 2 or position[1] < 0 or position[1] > 2:
        return False
    elif board[position[0]][position[1]] != '.':
        return False
    else:
        return True


def isEnd():
    # Vertical win
    for i in range(0, 3):
        if (board[0][i] != '.' and
            board[0][i] == board[1][i] and
                board[1][i] == board[2][i]):
            return board[0][i]
    # Horizontal win
    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'
    # Main diagonal win
    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
            board[0][0] == board[2][2]):
        return board[0][0]
    # Second diagonal win
    if (board[0][2] != '.' and
        board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
        return board[0][2]
    # Is whole board full?
    for i in range(0, 3):
        for j in range(0, 3):
            # There's an empty field, we continue the game
            if (board[i][j] == '.'):
                return None
    # It's a tie!
    return '.'


def play():
    global player_turn

    while True:
        printBoard()
        result = isEnd()

        if result != None:
            if result == 'X':
                print('The winner is X!')
            elif result == 'O':
                print('The winner is O!')
            elif result == '.':
                print("It's a tie!")

            clearBoard()
            return

        if player_turn == 'X':
            while True:
                start = time.time()
                position = [None, None]
                (m, position) = min_alpha_beta(-2, 2)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: X = {}, Y = {}'.format(
                    position[0], position[1]))

                position[0] = int(input('Insert the X coordinate: '))
                position[1] = int(input('Insert the Y coordinate: '))

                if isValid(position):
                    board[position[0]][position[1]] = 'X'
                    player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')

        else:
            (m, position) = max(-2, 2)
            board[position[0]][position[1]] = 'O'
            player_turn = 'X'


def max(alpha, beta):
    maxv = -2
    max_pos = [None, None]
    result = isEnd()

    if result == 'X':
        min_pos = [0, 0]
        return (-1, min_pos)
    elif result == 'O':
        min_pos = [0, 0]
        return (1, min_pos)
    elif result == '.':
        min_pos = [0, 0]
        return (0, min_pos)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                (m, min_pos) = min_alpha_beta(alpha, beta)
                if m > maxv:
                    maxv = m
                    max_pos = [i, j]
                board[i][j] = '.'
                # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                if maxv >= beta:
                    return (maxv, max_pos)
                if maxv > alpha:
                    alpha = maxv
    return (maxv, max_pos)


def min_alpha_beta(alpha, beta):
    minv = 2
    min_pos = [None, None]
    result = isEnd()
    if result == 'X':
        min_pos = [0, 0]
        return (-1, min_pos)
    elif result == 'O':
        min_pos = [0, 0]
        return (1, min_pos)
    elif result == '.':
        min_pos = [0, 0]
        return (0, min_pos)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                (m, max_pos) = max(alpha, beta)
                if m < minv:
                    minv = m
                    min_pos = [i, j]
                board[i][j] = '.'
                if minv <= alpha:
                    return (minv, min_pos)
                if minv < beta:
                    beta = minv
    return (minv, min_pos)


clearBoard()
global player_turn
player_turn = 'X'
play()
