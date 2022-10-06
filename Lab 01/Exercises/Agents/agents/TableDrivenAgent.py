A = 'A'
B = 'B'
percepts = []
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    # ...
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left',
    # ...
}


def look_up(percepts, table): # Lookup appropriate action for percepts
    action = table.get(tuple(percepts))
    return action


def table_driven_agent(percept):
    percepts.append(percept)
    action = look_up(percepts, table)
    return action


def run(): # run agent on several sequential percepts
    print('Action\tPercepts')
    print(table_driven_agent((A, 'Clean')), '\t', percepts)
    print(table_driven_agent((A, 'Dirty')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)


run()

'''
Task 2
for each new perceptions, the percepts get longer, because the agent function remembers 
the percept history of moves.

Task 3
How many table entries would be required if only the current percept 
was used to select an action rather than the percept history?

It will only require 2*2 = 4 entries, because there is only two spots and each spot only have 2 states.

Task 4
How many table entries are required for an agent lifetime of T steps?

there need to be one for every scenario so the requirement is 2t^2t because 
there is 2 different states (Clear and Dirty)
'''