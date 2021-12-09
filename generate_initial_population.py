from random import sample


def generate_random_individual(cities):
    """Receive a route and randomize it, ignoring the
    first and last element (origin and final destiny)."""
    randomized_route = sample(cities[1:-1], len(cities[1:-1]))
    cities[1:-1] = randomized_route
    return tuple(cities)


def generate_initial_population(cities, desired_population_number):
    """Creates an population list an individual. If the individual
    isn't in population list, the individual is added. The list is
    returned when list length is equal to the desired population
    number.
    """
    population = []
    while len(population) != desired_population_number:
        individual = generate_random_individual(cities)
        if individual not in population:
            population.append(individual)
    return population
