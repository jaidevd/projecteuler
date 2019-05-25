import numpy as np

x = open('p067_triangle.txt').readlines()
x = [l.rstrip().split() for l in x]
x = [list(map(int, l)) for l in x]
x = [np.array(l) for l in x]

S = 0

for i, l in enumerate(x):
    if i == 0:
        S += l[0]
        index = 0
    else:
        prevIndex = index
        left = prevIndex
        right = prevIndex + 1
        if l[right] > l[left]:
            index = right
        else:
            index = left
        S += l[index]
    print(l[index])

print(S)
