from get_population_fitness import get_population_fitness
from random import uniform


def select_individual_by_elitism(population, cities_coordinates):
    population_fitness = get_population_fitness(cities_coordinates, population)
    best_one = population_fitness[0]
    population_fitness = population_fitness[1:]
    return [best_one, population_fitness]


def select_individual_by_roulette_wheel(population, cities_coordinates):
    population_fitness = get_population_fitness(cities_coordinates, population)
    population_fitness_sum = 0

    for fit_value in population_fitness:
        population_fitness_sum += fit_value[1]

    individual_probabilities = []
    population_size = len(population)
    for individual_fitness in population_fitness:
        individual_probabilities.append((1 / (population_size - 1)) *
                                  (1 - (individual_fitness[1] / population_fitness_sum)))

    random_number = uniform(0, 1)
    for index in range(population_size):
        if random_number > individual_probabilities[index]:
            selected_individual = population_fitness[index]
            population.remove(selected_individual[0])
            return [selected_individual[0], population]
