from math import sqrt
import numpy as np
from itertools import permutations
from tqdm import tqdm


def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def triangle(n):
    return np.sum(range(1, n + 1))


def isperfect(n):
    ndivs = len(divisors(n))
    if n == np.sum(range(1, ndivs + 1)):
        return True
    return False


def isabundant(n):
    ndivs = len(divisors(n))
    if n < np.sum(range(1, ndivs + 1)):
        return True
    return False


def isdeficient(n):
    ndivs = len(divisors(n))
    if n > np.sum(range(1, ndivs + 1)):
        return True
    return False


def forty_primes():
    primes = []
    for x in range(40):
        primes.append(x ** 2 + x + 41)
    return primes


def eighty_primes():
    primes = []
    for x in range(80):
        primes.append(x ** 2 - 79 * x + 1601)
    return primes


def divisors(n):
    obv = [1, n]
    if isprime(n):
        return set(obv)
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            obv.extend([i, int(n / i)])
    return set(obv)


def carry_sum(l):
    x = str(sum(l))
    _sum = int(x[-1])
    carry = int(x[:-1])
    return carry, _sum


def pandigital_primes(n):
    digits = list(range(1, n + 1))
    perms = []
    for perm in tqdm(permutations(digits)):
        n = int(''.join(map(str, perm)))
        if isprime(n):
            perms.append(n)
    return perms


def pandigitals(low, high):
    digits = list(range(low, high + 1))
    for perm in permutations(digits):
        if perm[0] != 0:
            yield perm


def is_triangle(n):
    return (sqrt(1 + 8 * n) - 1) % 2 == 0


def is_pentagonal(n):
    return (sqrt(1 + 24 * n) + 1) % 6 == 0


def is_hexagonal(n):
    return (sqrt(1 + 8 * n) + 1) % 4 == 0
