
is_leap = lambda year: (year % 400 == 0) or (year % 4 == 0)

NDPM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def n_days(y, m):
    if m == 2 and is_leap(y):
        return 29
    return NDPM[m - 1]


def process_month(y, m, d):
    """Given first day of a month, find the first day of the next month."""
    ndpm = n_days(y, m)
    nd = d + ndpm % 7
    if nd > 6:
        nd = nd % 7
    return nd


s = 0
currentDay = 2
for year in range(1901, 2001):
    for month in range(1, 13):
        currentDay = process_month(year, month, currentDay)
        if currentDay == 0:
            s += 1

print(s)
