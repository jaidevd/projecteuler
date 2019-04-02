from math import log2


def collatz_series(n):
    count = 0
    while n > 1:
        count += 1
        l = log2(n)  # noqa: E741
        if l % 1 == 0:
            count += l - 1
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return count + 1
