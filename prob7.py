#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from misc import isprime

ix = 1
latestPrime = 2


def getNextPrime(n):
    while True:
        n += 1
        if isprime(n):
            break
    return n


while ix < 10001:
    latestPrime = getNextPrime(latestPrime)
    ix += 1

print(ix, latestPrime)
