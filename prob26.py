from decimal import Decimal, getcontext
from tqdm import tqdm

context = getcontext()
context.prec = 1024


def longest_prefix(x, y):
    lx, ly = map(len, (x, y))
    if lx < ly:
        if y[:lx] == x:
            return x
    if ly < lx:
        if x[:ly] == y:
            return y
    sub = []
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            sub.append(x[i])
        else:
            break
    return ''.join(sub)


def suffix_strings(s):
    y = [s[i:] for i in range(len(s))]
    y.sort()
    return y


def largest_subs(s):
    suf = suffix_strings(s)
    maxLen = 0
    for i in range(len(suf) - 1):
        longest = longest_prefix(suf[i], suf[i + 1])
        if len(longest) > maxLen:
            maxLen = len(longest)
    return maxLen


k = Decimal(1)
maxLen = [0]
for i in tqdm(range(2, 1000)):
    if 1000 % i == 0:
        continue
    x = k / Decimal(i)
    l = largest_subs(str(x)[2:])  # noqa
    maxLen.append(l)
