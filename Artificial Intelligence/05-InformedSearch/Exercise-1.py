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
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Price: ' + str(self.PRICE)


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
        s.STATE = (child[0], child[1])  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.PRICE = (child[1] * ALPHA) + child[2] + node.PRICE
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def INSERT(node: Node, queue: list):
    for i in range(len(queue)):
        if(node.PRICE < queue[i].PRICE):
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
        if smallest.PRICE > n.PRICE:
            smallest = n
    queue.remove(smallest)
    return smallest

'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


ALPHA = 1
INITIAL_STATE = ('A', 6)
GOAL_STATE = ('L', 0) or ('L', 0)
STATE_SPACE = {('A', 6): [('B', 5, 1), ('C', 5, 2), ('D', 2, 4)],
               ('B', 5): [('A', 6, 1), ('F', 5, 4), ('E', 4, 5)],
               ('C', 5): [('A', 6, 2), ('E', 4, 1)],
               ('D', 2): [('A', 6, 4), ('H', 1, 1), ('I', 2, 4), ('J', 1, 2)],
               ('F', 5): [('B', 5, 5), ('G', 4, 1)],
               ('E', 4): [('B', 5, 4), ('C', 5, 1), ('G', 4, 2), ('H', 1, 3)],
               ('I', 2): [('D', 2, 4), ('L', 0, 3)],
               ('G', 4): [('F', 5, 1), ('E', 4, 2), ('K', 0, 6)],
               ('H', 1): [('D', 2, 1), ('E', 4, 3), ('K', 0, 6), ('L', 0, 5)],
               ('J', 1): [('D', 2, 2)],
               ('K', 0): [('G', 4, 6), ('H', 1, 6)],
               ('L', 0): [('I', 2, 3), ('H', 1, 5)]
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
