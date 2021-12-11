from util import generate_split_points


def ordered_crossover(x1, x2):
    """Receive two chromosomes x1 and x2, and return their
    children y1 and y2, based on ordered crossover method."""
    x1, x2 = list(x1), list(x2)
    # saving R and removing it right after
    r = x1[:1]
    x1 = x1[1:-1]
    x2 = x2[1:-1]
    # chromosome length
    n = len(x1)
    # starting y1 and y2 as empty genotype children
    y1 = [None for _ in range(n)]
    y2 = y1.copy()

    # generating random crossover split points such as 0 <= a < b <= n
    point_a, point_b = generate_split_points(0, len(x1))

    # putting the inherited points to children chromosomes
    y1[point_a:point_b] = x2[point_a:point_b]
    y2[point_a:point_b] = x1[point_a:point_b]

    if point_b == n:
        # if the second crossover split point == n
        # the next index should be obligatorily 0
        j1 = j2 = k = 0
    else:
        # otherwise, starting point should be equal b
        j1 = j2 = k = point_b

    for i in range(n):
        if x1[k] not in x2[point_a:point_b]:
            y1[j1] = x1[k]
            # if the auxiliary variable reach n, the list index
            # starts from beginning otherwise, it just continues
            j1 = 0 if (j1 + 1) == n else j1 + 1
        if x2[k] not in x1[point_a:point_b]:
            y2[j2] = x2[k]
            j2 = 0 if (j2 + 1) == n else j2 + 1
        # k helps to control the current parent variable checked
        k = 0 if (k + 1) == n else k + 1
    # adding R back
    y1 = tuple(r + y1 + r)
    y2 = tuple(r + y2 + r)
    return [y2, y1]
