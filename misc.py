from math import sqrt
import numpy as np


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
