import selection
from get_cities_coordinates import get_cities_coordinates
from generate_initial_population import generate_initial_population

input_path = "C:/Users/lucas/Documents/BSI/PI2/input.txt"

if __name__ == '__main__':
    coordinates, route = get_cities_coordinates(input_path)

    population = generate_initial_population(cities=route, desired_population_number=8)
    selected = selection.selection(1, population, coordinates)
    print(selected)

