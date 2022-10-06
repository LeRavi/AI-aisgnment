A = 'A'
B = 'B'

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


def simple_reflex_agent(percept):  # Determine action
    state = interpret_input(percept)
    rule = rule_match(state, rules)
    action = RULE_ACTION[rule]
    return action


def sensors():  # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])


def actuators(action):  # modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A


def run(n):  # Run the agent through n steps
    print('Current             New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = sensors()  # Sense the environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = simple_reflex_agent(sensors())
        actuators(action)
        (location, status) = sensors()  # Sense Environment after action
        print("{:8}{:12s}{:8s}".format(action, location, status))


run(10)

'''
Task 3
Yes, the actuators allow bogus actions, if rule "(A, 'Clean'): 2" is changed to 3 (left), 
the actuators keep trying to go to left. 

Excercise 3
Yes, if the condition-action rule   " 2: 'Right' " is changed to "Left", then the actuators will keep trying to 
go left.
'''