# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import sys
from datetime import datetime

maximum = int(sys.argv[1])

def sieve_list_first_n(firstN):
    primes = [2]
    for n in range(3, sys.maxsize, 2):
        isPrime = True
        for p in primes:
            isPrime = n % p != 0
            if not isPrime or p*p > n:
                break
        if isPrime:
            primes.append(n)
            # print(primes[-10:])
        if len(primes) >= firstN:
            break
    return primes

start = datetime.now()
print(sieve_list_first_n(maximum)[-1])
print('completed in {} seconds'.format((datetime.now() - start).total_seconds()))
