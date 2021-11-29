
from calculate_distance import calculate_route_distance


def calculate_fitness(cities_coordinates, cities_route):
    route_distance_cost = calculate_route_distance(cities_coordinates, cities_route)
    return 1 / float(route_distance_cost)


def get_population_fitness(cities_coordinates, population):
    population_fitness = {}
    for individual in population:
        population_fitness[individual] = calculate_fitness(cities_coordinates, individual)
    return sorted(population_fitness.items(),
                  key=lambda get_elem: get_elem[1],
                  reverse=True)
