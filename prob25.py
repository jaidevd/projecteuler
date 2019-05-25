cache = {1: 1, 2: 1}


def fib(n):
    if n in cache:
        return cache[n]
    N = fib(n - 1) + fib(n - 2)
    cache[n] = N
    return N


i = 1
while True:
    nd = len(str(fib(i)))
    if nd == 1000:
        break
    i += 1


print(i)
