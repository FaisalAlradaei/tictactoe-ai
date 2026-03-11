import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def player(board):
    x = 0
    o = 0

    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            if cell == O:
                o += 1

    if x == o:
        return X
    else:
        return O


def actions(board):
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    new_board = copy.deepcopy(board)

    i = action[0]
    j = action[1]

    if new_board[i][j] != EMPTY:
        raise Exception("Invalid move")

    new_board[i][j] = player(board)

    return new_board


def winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):

    if winner(board) != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):

    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):

    if terminal(board):
        return None

    turn = player(board)

    best_move = None

    if turn == X:
        best_score = -100

        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action

    else:
        best_score = 100

        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action

    return best_move


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -100

    for action in actions(board):
        value = min_value(result(board, action))
        if value > v:
            v = value

    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = 100

    for action in actions(board):
        value = max_value(result(board, action))
        if value < v:
            v = value

    return v