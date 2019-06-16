from misc import is_pentagonal, is_hexagonal

triangle = lambda x: x * (x + 1) / 2

start = 286
while True:
    new = triangle(start)
    if is_hexagonal(new):
        if is_pentagonal(new):
            break
    start += 1

print(new)
