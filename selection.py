from get_population_fitness import get_population_fitness
from random import uniform


def elitism_selection(desired_individuals_number, population, cities_coordinates):
    """Receive a population list and its coordinates. Then, calculate
    it fitness and return a list containing the individual with the best
    fitness value, besides that, the population without the selected one."""
    population_fitness = get_population_fitness(cities_coordinates, population)
    selected = []
    for i in range(desired_individuals_number):
        best_current = population_fitness[i]
        selected.append(best_current[0])
        population.remove(best_current[0])
    return [selected, population]


def roulette_wheel_selection(population, cities_coordinates):
    """Receive a population list and its coordinates. Then, return a
    list containing the first selected individual based on roulette
    wheel selection."""
    population_fitness = get_population_fitness(cities_coordinates, population)
    population_fitness_sum = 0

    for fit_value in population_fitness:
        population_fitness_sum += fit_value[1]

    individual_probabilities = []
    population_size = len(population)
    for individual_fitness in population_fitness:
        individual_probabilities.append((1 / (population_size - 1)) *
                                  (1 - (individual_fitness[1] / population_fitness_sum)))

    selected_individuals = []

    for index in range(population_size):
        random_number = uniform(0, 1)
        if random_number > individual_probabilities[index]:
            selected_individual = population_fitness[index]
            selected_individuals.append(selected_individual[0])
    return selected_individuals


def selection(desired_elite_number, population, cities_coordinates):
    """Do the selection process mixing roulette and elitism method."""
    elitism_individuals, population = elitism_selection(desired_elite_number, population, cities_coordinates)
    roulette_individuals = roulette_wheel_selection(population, cities_coordinates)
    return elitism_individuals + roulette_individuals
