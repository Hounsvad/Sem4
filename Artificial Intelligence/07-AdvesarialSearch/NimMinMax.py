def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        #print('V: ' + str(v))
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
    return state


def is_terminal(state: list):
    for i in range(len(state)): #Game is terminal if all piles are smaller than 3 as one cant split into equal parts.
        pile = state[i]
        if pile >= 3:
            return False
    return True


def utility_of(state):
    itemcount = 0
    for i in state:
        itemcount += 1
    if itemcount % 2 == 1:
        return -1
    else:
        return 1


def successors_of(state):
    successors = []
    for i in range(len(state)):  #Handle each availible pile
        pile = state[i]

        if pile >= 3:  #Allow for a split
            for pile1 in range(pile - 1):
                newState = state[:]
                if pile - pile1 != pile1 and pile1 != 0 and pile1 != pile:
                    newState.append(pile1)
                    newState.append(pile-pile1)
                    newState.remove(pile)
                    successors.append((i, newState))
    return successors



def display(state):
    print("-----")
    print(state)

def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles

def main():
    piles = [15]
    winner = 0
    while not is_terminal(piles):
        piles = minmax_decision(piles)
        if not is_terminal(piles):
            piles = user_select_pile(piles)
        else:
            winner = utility_of(piles)

    players = {-1:"Human", 1:"AI"}
    print("Player ", players[winner], " Won")
    display(piles)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
