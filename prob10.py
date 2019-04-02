#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from misc import isprime


def getNextPrime(n):
    while True:
        n += 1
        if isprime(n):
            break
    return n


s = 0
latestPrime = 2

while latestPrime < 2000000:
    s += latestPrime
    latestPrime = getNextPrime(latestPrime)

print(s)
