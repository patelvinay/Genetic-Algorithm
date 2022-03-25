import random

def create_individual(length):
    return [random.randint(0, 1) for x in range(length)]

def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if i < len(parent1) / 2:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < 0.1:
            individual[i] = 1 - individual[i]

def create_population(size, length):
    return [create_individual(length) for x in range(size)]

def calculate_fitness(individual):
    # calculate the number of ones in the individual
    return individual.count(1)

def main():
    length = 10
    population_size = 20
    num_generations = 100

    population = create_population(population_size, length)

    for generation in range(num_generations):
        print('Generation: ' + str(generation))
        print('Population: ' + str(population))

        # calculate fitness of each individual in the population
        fitness = [calculate_fitness(x) for x in population]

        # select two parents based on fitness
        parent1 = population[fitness.index(max(fitness))]
        fitness.pop(fitness.index(max(fitness)))
        parent2 = population[fitness.index(max(fitness))]
        fitness.pop(fitness.index(max(fitness)))

        # create child through crossover
        child = crossover(parent1, parent2)

        # mutate child
        mutate(child)

        # replace least fit individual in population with child
        population.pop(fitness.index(min(fitness)))
        population.append(child)

    print('Final population: ' + str(population))

if __name__ == '__main__':
    main()