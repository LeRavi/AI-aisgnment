def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


X = 'X'
O = 'O'


def is_move(move):
    return type(move) == int


def tree_in_a_row(line):
    return line[0] == line[1] == line[2]


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    is_terminated = False

    for move in state:
        if is_move(move):
            is_terminated = False
        else:
            is_terminated = True

    psbl_line = [
        (state[0], state[1], state[2]),
        (state[3], state[4], state[5]),
        (state[6], state[7], state[8]),
        (state[0], state[3], state[6]),
        (state[1], state[4], state[7]),
        (state[2], state[5], state[8]),
        (state[0], state[4], state[8]),
        (state[2], state[4], state[6]),
    ]

    for line in psbl_line:
        if tree_in_a_row(line):
            is_terminated = True

    return is_terminated


def utility_of(state):

    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    x_win = False
    o_win = False

    psbl_line = [
        (state[0], state[1], state[2]),
        (state[3], state[4], state[5]),
        (state[6], state[7], state[8]),
        (state[0], state[3], state[6]),
        (state[1], state[4], state[7]),
        (state[2], state[5], state[8]),
        (state[0], state[4], state[8]),
        (state[2], state[4], state[6]),
    ]

    for line in psbl_line:
        if tree_in_a_row(line):
            res = line[0]
            if res == X:
                x_win = True
            elif res == O:
                o_win = True

    if x_win:
        return 1
    elif o_win:
        return -1

    else:
        return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    list_successor_states = []

    odd_or_even = 0
    for move in state:
        if is_move(move):
            odd_or_even += 1

    x = False
    o = False

    if odd_or_even % 2 == 0:
        o = True
    else:
        x = True

    for i in range(9):

        move = state[i]
        if is_move(state[i]):

            new_state = state[:]
            if o:
                new_state[move] = O
            elif x:
                new_state[move] = X
            list_successor_states.append((move, new_state))

    return list_successor_states


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
