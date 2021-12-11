from util import generate_split_points
from random import uniform


def reverse_sequence_mutation(x, mutation_chance):
    """Receive a chromosome x and return a mutated version
    or not, based on the mutation rate received."""
    # saving R and removing it right after
    r = list(x[:1])
    x = list(x)[1:-1]

    # verifying if the mutation will occur
    random_number = uniform(0, 1)
    if random_number <= mutation_chance:
        # generating random crossover split points such as 0 <= a < b <= n
        point_a, point_b = generate_split_points(0, len(x)-1)

        # reverting the sequence
        while point_a < point_b:
            x[point_a], x[point_b] = x[point_b], x[point_a]
            point_a += 1
            point_b -= 1

    x = tuple(r + x + r)
    return x
