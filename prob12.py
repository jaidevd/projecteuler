import misc
import numpy as np

def get_solution():
    n = 0
    while True:
        n += 1
        divs = len(misc.divisors(n))
        if n%1000 == 0:
            print n, divs
        if divs > 499:
            return n

class FactorCache(object):
    
    def __init__(self, value=None):
        self.value = value
        self.cache = {}
    
    def divisors(self, n):
        ndivs = 0
        for i in range(1, int(np.floor(n/2))+1):
            if str(i) in self.cache.keys():
                ndivs += self.cache[str(i)]
            elif self.value%i ==0:
                ndivs += 1
        self.cache[str(n)] = ndivs


if __name__ == "__main__":
    print get_solution()