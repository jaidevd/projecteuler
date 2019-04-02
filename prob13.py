with open('prob13.txt', 'r') as fout:
    data = [x.lstrip().rstrip() for x in fout.readlines()]

carry = 0
acc = []
for i in range(50):
    digits = map(int, [x[-(i + 1)] for x in data])
    s = sum(digits) + carry
    carry = int(str(s)[:-1])
    if i < 49:
        acc.append(str(s)[-1])
    else:
        acc.append(str(s))

print("".join(acc[::-1])[:10])
print(sum(map(int, data)))
