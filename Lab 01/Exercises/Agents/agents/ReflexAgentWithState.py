A = 'A'
B = 'B'
state = {}
action = None
model = {A: None, B: None}

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}
# Ex. rule (if location == A && Dirty then rule 1)

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def interpret_input(input):  # no interpretation
    return input


def rule_match(state, rules):  # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule


def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == 'Clean':
        state = (A, B, 'Clean')
        #  model consulted only for A and B Clean
    model[location] = status  # Update the model state
    return state


def reflex_agent_with_state(percept):
    global state, action
    state = update_state(state, action, percept)
    rule = rule_match(state, rules)
    action = RULE_ACTION[rule]
    return action


def sensors():  # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])


def actuators(action):  # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A


def run(n):  # run the agent trough n steps
    print('Current             New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = reflex_agent_with_state(sensors())
        actuators(action)
        (location, status) = sensors()  # Sense Environment after action
        print("{:8}{:12s}{:8s}".format(action, location, status))
