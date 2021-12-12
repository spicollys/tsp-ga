
from calculate_distance import calculate_route_distance


def calculate_fitness(cities_coordinates, cities_route):
    """Return the inverse of the route distance cost."""
    route_distance_cost = calculate_route_distance(cities_coordinates, cities_route)
    return 1 / float(route_distance_cost)


def get_population_fitness(cities_coordinates, population):
    """Return a ordered list of tuples containing the respective
     route and its fitness, for each individual of a population. """
    population_fitness = []
    for individual in population:
        population_fitness.append((individual, calculate_fitness(cities_coordinates, individual)))
    return sorted(population_fitness,
                  key=lambda get_elem: get_elem[1])
