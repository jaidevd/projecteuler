import math


def gen_pythagorean_triple(n):
    triples = []
    for i in range(1, n + 1):
        k = 2 * i - 1
        a = math.sqrt(k)
        if a % 1 != 0:
            continue
        b, c = i - 1, i
        triple = (a, b, c)
        triples.append(triple)
        multiplier = 2
        while True:
            new_triple = [multiplier * j for j in triple]
            if sum(new_triple) <= n:
                triples.append(new_triple)
                multiplier += 1
            else:
                break
    return [t for t in triples if sum(t) == n]
