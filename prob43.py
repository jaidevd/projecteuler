from misc import pandigitals

rules = [
    (1, 4, 2),
    (2, 5, 3),
    (3, 6, 5),
    (4, 7, 7),
    (5, 8, 11),
    (6, 9, 13),
    (7, 10, 17)
]


def checker(number, rule):
    low, high, divisor = rule
    number = int(''.join(map(str, number[low:high])))
    return number % divisor == 0


s = 0
for p in pandigitals(0, 9):
    is_valid = True
    for r in rules:
        if not checker(p, r):
            is_valid = False
            break
    if is_valid:
        s += int(''.join(map(str, p)))
print(s)
