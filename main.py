from generate_next_population import generate_next_population
from get_cities_coordinates import get_cities_coordinates
from generate_initial_population import generate_initial_population

input_path = "C:/Users/lucas/Documents/BSI/PI2/input.txt"

if __name__ == '__main__':
    coordinates, route = get_cities_coordinates(input_path)

    population = generate_initial_population(cities=route, desired_population_number=8)
    population_number = 20

    for _ in range(population_number):
        population = generate_next_population(population=population,
                                              desired_elite_number=2,
                                              mutation_chance=0.01,
                                              cities_coordinates=coordinates)

    print(population[0])
