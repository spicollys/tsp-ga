import selection
from crossover import ordered_crossover
from get_cities_coordinates import get_cities_coordinates
from generate_population import generate_population

input_path = "C:/Users/lucas/Documents/BSI/PI2/input.txt"

if __name__ == '__main__':
    coordinates, route = get_cities_coordinates(input_path)

    population = generate_population(cities=route, desired_population_number=4)
    x1, population = selection.select_individual_by_roulette_wheel(cities_coordinates=coordinates, population=population)
    x2, population = selection.select_individual_by_roulette_wheel(cities_coordinates=coordinates, population=population)
    print(x1, x2)
    y1, y2 = ordered_crossover(x1, x2)
    print(y1, y2)