#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from misc import isprime

n = 600851475143
while n > 1:
    latestPrime = 2
    for i in range(latestPrime, n // latestPrime + 1):
        if n % i == 0:
            if isprime(i):
                latestPrime = i
                n = n / i
                print(latestPrime)
