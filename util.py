from random import randint


def generate_split_points(begin, end):
    """Generates two integers a e b between
    (and including) begin and end parameters,
    such as begin <= a < b <= end"""
    point_a = point_b = 0

    while point_a == point_b:
        point_a = randint(begin, end)
        point_b = randint(begin, end)

        if point_a > point_b:
            point_a, point_b = point_b, point_a

    return [point_a, point_b]
