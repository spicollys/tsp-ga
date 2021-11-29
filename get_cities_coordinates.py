def get_cities_coordinates(file_path):
    """Read a file and return a dict of tuples containing
     all cities (letters) and respectively positions.
    Input example, for lines == 4 and columns == 5:

        0 0 0 0 D
        0 A 0 0 0
        0 0 0 0 C
        R 0 0 B 0

    Output:
    {'D': (0, 4), 'A': (1, 1), 'C': (2, 4), 'R': (3, 0), 'B': (3, 2)}
    """
    cities_position = {}
    with open(file_path) as f:
        text_file = f.readlines()
        lines, columns = map(int, text_file[0].split())
        for i in range(1, lines + 1):
            line = text_file[i].split()
            for j in range(columns):
                if line[j] != '0':
                    cities_position[line[j]] = (i-1, j)
    ordered_route = sorted(list(cities_position))
    return [cities_position, ['R'] + ordered_route]
