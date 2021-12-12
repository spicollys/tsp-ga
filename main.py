from calculate_distance import calculate_route_distance
from generate_next_population import generate_next_population
from get_cities_coordinates import get_cities_coordinates
from generate_initial_population import generate_initial_population
import matplotlib.pyplot as plt

input_path = "C:/Users/lucas/Documents/BSI/PI2/input.txt"


def genetic_algorithm(input_file_path, desired_population_number, number_of_generations, desired_elite_number, mutation_chance):
    coordinates, route = get_cities_coordinates(input_file_path)

    population = generate_initial_population(cities=route,
                                             desired_population_number=desired_population_number)
    best_cost_by_generation = []
    best_one = None
    for generation in range(number_of_generations):
        population = generate_next_population(population=population,
                                              desired_elite_number=desired_elite_number,
                                              mutation_chance=mutation_chance,
                                              cities_coordinates=coordinates)

        best_one = population[0]
        best_cost_by_generation.append(calculate_route_distance(coordinates, best_one))

    print(best_one)
    plt.figure(figsize=(12, 6), dpi=80).gca()
    plt.rcParams["figure.autolayout"] = True
    with plt.rc_context({'lines.linewidth': 2, 'lines.linestyle': '-'}):
        plt.plot(best_cost_by_generation, 'r-o')
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()


if __name__ == '__main__':
    genetic_algorithm(input_file_path=input_path,
                      desired_population_number=8,
                      number_of_generations=50,
                      desired_elite_number=0,
                      mutation_chance=0.01)
