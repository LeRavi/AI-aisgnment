def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for state in successors_of(state):
            v = max(v, min_value(state))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for state in successors_of(state):
            v = min(v, max_value(state))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state


def is_terminal(state):

    for pile in state:
        if pile >= 3:
            return False
    return True


def utility_of(state):
    if len(state) % 2 == 0:
        return -1
    else:
        return 1


def successors_of(state):

    r_states = []

    for pile in state:
        if pile >= 3:
            index = 0
            if pile % 2 == 0:
                index = int(pile / 2)
            else:
                index = int(pile/2 + 1)

            for i in range(1, index):
                nw_state = state[:]
                nw_state.remove(pile)
                nw_state.append(i)
                nw_state.append(pile-i)
                r_states.append(nw_state)

    return r_states


def display(state):
    print(state)


def main():
    state = [15]
    while not is_terminal(state):
        state = minmax_decision(state)
        if not is_terminal(state):
            display(state)
            split_pile = int(input(" which pile to split ? "))
            pile = state[split_pile]
            pile_one = int(input(" size of pile one? "))
            pile_two = pile - pile_one

            state.remove(pile)
            state.append(pile_one)
            state.append(pile_two)
            display(state)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
