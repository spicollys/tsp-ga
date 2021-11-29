import selection
from calculate_distance import calculate_route_distance
from get_cities_coordinates import get_cities_coordinates
from generate_population import generate_individual, generate_population
from get_population_fitness import get_population_fitness

input_path = "C:/Users/lucas/Documents/BSI/PI2/input.txt"

if __name__ == '__main__':
    coordinates, route = get_cities_coordinates(input_path)
    """print(
        calculate_fitness(
            cities_coordinates=coordinates,
            cities_route=generate_individual(route)
        )
    )"""

    population = generate_population(cities=route, desired_population_number=4)
    # print(population)
    # print(get_population_fitness(cities_coordinates=coordinates, population=population))
    print(selection.select_individual_by_roulette_wheel(cities_coordinates=coordinates, population=population))
