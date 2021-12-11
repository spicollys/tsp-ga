from selection import elitism_selection, roulette_wheel_selection
from crossover import ordered_crossover
from mutation import reverse_sequence_mutation


def generate_next_population(population, mutation_chance, desired_elite_number, cities_coordinates):
    population_length = len(population)
    next_population = []

    # selecting and adding the individuals by elitism
    elitism_individuals, population = elitism_selection(desired_elite_number, population, cities_coordinates)
    next_population += elitism_individuals

    # selecting the individuals by roulette method
    roulette_individuals = roulette_wheel_selection(population, cities_coordinates)

    # breeding the individuals using the selected ones as parents
    while len(next_population) < population_length:
        end = -1
        for begin in range(len(roulette_individuals)):
            x1 = roulette_individuals[begin]
            x2 = roulette_individuals[end]
            y1, y2 = ordered_crossover(x1, x2)
            # applying mutation
            y1 = reverse_sequence_mutation(y1, mutation_chance)
            y2 = reverse_sequence_mutation(y2, mutation_chance)
            end -= 1
            next_population.append(y1) if len(next_population) < population_length else []
            next_population.append(y2) if len(next_population) < population_length else []
    return next_population
