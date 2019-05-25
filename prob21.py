import misc


def d(n):
    return sum(misc.divisors(n) - {n})


def is_amicable(n):
    x = d(n)
    if x == n:
        return False
    return d(x) == n


s = 0
for i in range(2, 10001):
    if is_amicable(i):
        s += i

print(s)
