def subtract(a,b):
    y = next(b)
    x = next(a)
    while True:
        if x < y:
            yield x
            x = next(a)
        elif x > y:
            y = next(b)
        else:
            x = next(a)

from itertools import count, islice

def primes():
    yield 2
    sieve = count(3,2)
    while True:
        p = next(sieve)
        sieve = subtract(sieve, count(p*p,p))
        yield p

i = 100

for prime in primes():
    print(prime)
    i -= 1
    if not i:
        break
