from util import generate_split_points


def reverse_sequence_mutation(x):
    r = list(x[:1])
    x = list(x)[1:-1]

    point_a, point_b = generate_split_points(0, len(x))

    while point_a < point_b:
        x[point_a], x[point_b] = x[point_b], x[point_a]
        point_a += 1
        point_b -= 1

    x = tuple(r + x + r)
    return x
