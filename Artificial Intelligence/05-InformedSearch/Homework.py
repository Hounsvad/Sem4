# Deapth first

class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, price=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.PRICE = price

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_CHEAPEST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def INSERT(node: Node, queue: list):
    for i in range(len(queue)):
        if (node.PRICE < queue[i].PRICE):
            queue.insert(i, node)
            return queue
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''


def INSERT_ALL(list, queue):
    for n in list:
        INSERT(n, queue)
    return queue


'''
Removes and returns the first element from fringe
'''


def REMOVE_CHEAPEST(queue: list):
    smallest = queue[0]
    for n in queue:
        if smallest.DEPTH > n.DEPTH:
            smallest = n
    queue.remove(smallest)
    return smallest


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


ALPHA = 1
INITIAL_STATE = ('A', 'dirty', 'dirty')
GOAL_STATE = ('A', 'clean', 'clean') or ('B', 'clean', 'clean')
STATE_SPACE = {('A', 'dirty', 'dirty'): [('A', 'clean', 'dirty'), ('B', 'dirty', 'dirty')],
               ('A', 'dirty', 'clean'): [('A', 'clean', 'clean'), ('B', 'dirty', 'clean')],
               ('A', 'clean', 'dirty'): [('B', 'clean', 'dirty')],
               ('A', 'clean', 'clean'): [],
               ('B', 'dirty', 'dirty'): [('B', 'dirty', 'clean'), ('A', 'dirty', 'dirty')],
               ('B', 'dirty', 'clean'): [('A', 'dirty', 'clean')],
               ('B', 'clean', 'dirty'): [('B', 'clean', 'clean'), ('A', 'clean', 'dirty')],
               ('B', 'clean', 'clean'): [],
               }

'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
