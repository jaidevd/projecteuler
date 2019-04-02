import numpy as np
import misc


def test_isprime():
    # pick random primes from the first 10k primes
    X = np.loadtxt('primes_10k.txt').ravel().astype(int)
    X = np.random.choice(X, (100,), False)
    for i in X:
        assert misc.isprime(i)
