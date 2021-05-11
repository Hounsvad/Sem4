from queens_fitness import fitness_fn_positive, fitness_fn_negative

import random


p_mutation = 0.2
num_of_generations = 100


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()
        print("Pop Before growth: ", len(population))
        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)
        print("Pop after growth: ", len(population))
        population = thanos(population, fitness_fn)
        print("Pop after thanos: ", len(population))
        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break


    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual

def thanos(population, fitness_fn):
    sortedList = []
    for i in population:
        if len(sortedList) > 0:
            for j in range(0, len(sortedList)-1):
                if fitness_fn(sortedList[j]) < fitness_fn(i):
                    sortedList.insert(j, i)
                    break
            if i not in sortedList:
                sortedList.append(i)
        else:
            sortedList.append(i)
    return set(sortedList[:MAX_POP_SIZE])


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    child = []
    randomed = random.randint(0, BOARD_SIZE - 1)
    return tuple(mother[:randomed] + father[randomed:])



def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    ind = list(individual)
    ind[random.randint(0,len(ind)-1)] = random.randint(0,len(ind))

    return tuple(ind)



def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    fitness = []
    sumFit = 0
    for i in ordered_population:
        fitAmount = fitness_fn_positive(i)
        sumFit += fitAmount
        for f in range(fitAmount):
            fitness.append(i)
    returnList = []
    for k in range(2):
        returnList.append(fitness[random.randint(0, sumFit-1)])




    return returnList


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, n) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    initial_population = get_initial_population(BOARD_SIZE, STARTING_POP_SIZE)

    fittest = genetic_algorithm(initial_population, fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))

BOARD_SIZE = 8
STARTING_POP_SIZE = 2000
MAX_POP_SIZE = 1000


if __name__ == '__main__':
    pass
    main()

