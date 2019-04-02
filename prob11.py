#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import numpy as np


def parseGrid(x):
    return max(x.prod(0).max(), x.prod(1).max(), np.prod(np.diag(x)),
               np.prod(np.diag(np.fliplr(x))))


x = np.loadtxt('p11grid.txt')
maxYet = 1
for i in range(16):
    for j in range(16):
        grid = x[i:(i + 4), j:(j + 4)]
        y = parseGrid(grid)
        if y > maxYet:
            maxYet = y

print(maxYet)
