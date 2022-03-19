"""
Write a generator, genPrimes, that returns the sequence of prime numbers on
successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""


def genPrimes():
    primes = []
    last = 1
    while True:
        last += 1
        for i in primes:
            if last % i == 0:
                break
        else:
            primes.append(last)
            yield last
