

def calculate_route_distance(cities_coordinates, cities_route):
    """Receive a dict of coordinates and an arbitrary city
    route. So, the route cost and the route is returned."""
    route_distance_cost = 0
    for city in range(len(cities_route)-1):
        current_city_coordinate = cities_coordinates[cities_route[city]]
        next_city_coordinate = cities_coordinates[cities_route[city + 1]]

        route_distance_cost += calculate_distance_between_two_cities(
            current_city_coordinate,
            next_city_coordinate)
    return route_distance_cost


def calculate_distance_between_two_cities(coordinates_city_a, coordinates_city_b):
    """Receive coordinates from two different cities
    and return the distance between these two."""
    distance = abs(coordinates_city_a[0] - coordinates_city_b[0]) + abs(
        coordinates_city_a[1] - coordinates_city_b[1])
    return distance
