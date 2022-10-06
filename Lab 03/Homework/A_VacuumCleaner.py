A = "A"
B = "B"
CLEAN = "CLEAN"
DIRTY = "DIRTY"

HEURISTIC = {
    (A, CLEAN, CLEAN): 0,
    (B, CLEAN, CLEAN): 0,
    (A, CLEAN, DIRTY): 1,
    (A, DIRTY, CLEAN): 1,
    (B, CLEAN, DIRTY): 1,
    (B, DIRTY, CLEAN): 1,
    (B, DIRTY, DIRTY): 2,
    (A, DIRTY, DIRTY): 2
}


class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, heuristic, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTIC = heuristic
        self.LENGTH = heuristic

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Length: ' + str(self.LENGTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def tree_search():
    fringe = []
    initial_node = Node(INITIAL_STATE, HEURISTIC[INITIAL_STATE])
    fringe = insert(initial_node, fringe)
    while fringe is not None:
        node = remove_lowest(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = expand(node)
        fringe = insert_all(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def expand(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node, HEURISTIC[(child[0], child[1], child[2])])
        s.STATE = (child[0], child[1], child[2])
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        temporary = STATE_SPACE[s.PARENT_NODE.STATE]
        temporary_length = 0
        for child in temporary:
            if (child[0], child[1], child[2]) == s.STATE:
                temporary_length = child[3]
        s.LENGTH = s.HEURISTIC + temporary_length + s.PARENT_NODE.LENGTH
        successors = insert(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def insert(node, queue):
    queue.append(node)
    return queue

'''
Insert list of nodes into the fringe
'''


def insert_all(list, queue):
    queue.extend(list)
    return queue


'''
Removes the lowest 
'''
def remove_lowest(fringe):
    if len(fringe) != 0:
        lowest = fringe[0]
        for node in fringe:
            if node.LENGTH < lowest.LENGTH:
                lowest = node
        fringe.remove(lowest)
    return lowest


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]


INITIAL_STATE = (A, DIRTY, DIRTY)
GOAL_STATE = (B, CLEAN, CLEAN)
STATE_SPACE = {(A, CLEAN, CLEAN): [(B, CLEAN, CLEAN, 1)],
               (B, CLEAN, CLEAN): [(A, CLEAN, CLEAN, 1)],
               (A, CLEAN, DIRTY): [(B, CLEAN, DIRTY, 1)],
               (B, DIRTY, CLEAN): [(A, DIRTY, CLEAN, 1)],
               (A, DIRTY, CLEAN): [(A, CLEAN, CLEAN, 1), (B, DIRTY, CLEAN, 1)],
               (B, CLEAN, DIRTY): [(B, CLEAN, CLEAN, 1), (A, CLEAN, DIRTY, 1)],
               (A, DIRTY, DIRTY): [(B, DIRTY, DIRTY, 1), (A, CLEAN, DIRTY, 1)],
               (B, DIRTY, DIRTY): [(A, DIRTY, DIRTY, 1), (B, DIRTY, CLEAN, 1)]}


'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = tree_search()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()


'''
Solution path:
State: ('B', 'CLEAN', 'CLEAN') - Depth: 3 - Length: 7
State: ('B', 'CLEAN', 'DIRTY') - Depth: 2 - Length: 6
State: ('A', 'CLEAN', 'DIRTY') - Depth: 1 - Length: 4
State: ('A', 'DIRTY', 'DIRTY') - Depth: 0 - Length: 2
'''
