from math import pi
import numpy as np

def isprime(n):
    for i in range(2, int(np.floor(np.sqrt(n))+1)):
        if n%i == 0:
            return False
    return True

def triangle(n):
    return np.sum(range(1,n+1))

def divisors(n):
    divs = []
    for i in range(1,int(np.floor(n/2))+1):
        if n%i == 0:
            divs.append(i)
    return divs

def isperfect(n):
    ndivs = len(divisors(n))
    if n == np.sum(range(1,ndivs+1)):
        return True
    return False

def isabundant(n):
    ndivs = len(divisors(n))
    if n < np.sum(range(1,ndivs+1)):
        return True
    return False

def isdeficient(n):
    ndivs = len(divisors(n))
    if n > np.sum(range(1,ndivs+1)):
        return True
    return False

def forty_primes():
    primes = []
    for x in range(40):
        primes.append(x**2 + x + 41)
    return primes

def eighty_primes():
    primes = []
    for x in range(80):
        primes.append(x**2 -79*x + 1601)
    return primes

class Number(object):
    
    def __init__(self, value=0):
        self.value = value
        self.isprime = isprime(value)
        self.perfect = isperfect(value)
        self.isabundant = isabundant(value)
        self.isdeficient = isdeficient(value)
        self.divisors = divisors(value)