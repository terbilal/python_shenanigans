#!/usr/bin/env python3
import math

# a prime number is only divisible by itself and 1
# define divs for divisibles of the number from 1 to round(math.sqrt(number))
def divlist (num):
    divs = []
    for div in range(1, round(math.sqrt(num))):
        if (num % div) == 0:
            divs.append(div)
            divs.append(int(num / div))
    divs.sort()
    return divs

primes = [1, 2]
for n in range (1, 1_000_000_000_000):
    if len(divlist(n)) == 2:
        print (n, end=" ")
