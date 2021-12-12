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
    population_fitness_sum = sum([fit_value[1] for fit_value in population_fitness])

    population_size = len(population)

    selected_individuals = []

    # selecting the individual according it probability
    random_number = uniform(0, population_fitness_sum)
    current_probability = 0
    for index in range(population_size):
        current_probability += population_fitness[index][1]
        if current_probability > random_number:
            selected_individual = population_fitness[index]
            selected_individuals.append(selected_individual[0])
    return selected_individuals
