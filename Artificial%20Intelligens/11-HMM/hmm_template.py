import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    forward = np.zeros((states.size, len(observations)))
    for p in range(1, states.size):
        forward[p][1] = transitions[0][p] * emissions[p][observations[1]]

    for o in range(2, len(observations)):
        for s in range (1, states.size):
            sum = 0
            for ss in range(1, states.size):
                sum += forward[ss][0-1] * transitions[ss][s] * emissions[s][observations[o]]
            forward[s][o] = sum
    totalSum = 0
    for s in range(1, states.size):
        totalSum += forward[s][len(observations) - 1] * transitions[s][states.size - 1]
    forward[states.size - 1][len(observations) - 1] = totalSum
    return forward[states.size - 1][len(observations) - 1]



def compute_viterbi(states, observations, transitions, emissions):
    T = len(observations)
    N = states.size
    viterbi = np.zeros((N, T))
    backpointer = np.zeros((N, T))
    for s in range(1, len(states)):
        viterbi[s][1] = transitions[0][s] * emissions[s][observations[1]]
        backpointer[s][1] = 0
    for t in range(2, T):
        for s in range(1, N - 1):
            probabilities_list = []
            backpointer_list = N * [0]
            for ss in range(1, N):
                probabilities_list.append(viterbi[ss][t-1] * transitions[ss][s] * emissions[s][observations[1]])
                backpointer_list[ss] = viterbi[ss][t-1] * transitions[ss][s]
            viterbi[s][t] = max(probabilities_list)
            backpointer[s][t] = argmax(backpointer_list)
    final_list = []
    final_backpointer_list = N * [0]
    for s in range(1, N):
        final_list.append(viterbi[s, T - 1] * transitions[s][N-1])
        final_backpointer_list[s] = viterbi[s, T - 1] * transitions[s][N-1]
    viterbi[N - 1][T - 1] = max(final_list)
    backpointer[N-1][T - 1] = argmax(final_backpointer_list)
    path = T * [0]
    path[0] = int(backpointer[N-1][T - 1])
    for t in range(1, T):
        path[t] = int(backpointer[path[t-1]][len(observations) - t])

    path.reverse()
    state_path = []
    for state_index in path:
        state_path.append(states[state_index])
    return state_path


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))
    return max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
