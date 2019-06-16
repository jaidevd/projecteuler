start = 0

while True:
    start += 1
    if set(str(start)) != set(str(2 * start)):
        continue
    if set(str(start)) != set(str(3 * start)):
        continue
    if set(str(start)) != set(str(4 * start)):
        continue
    if set(str(start)) != set(str(5 * start)):
        continue
    if set(str(start)) != set(str(6 * start)):
        continue
    break

print(start)
