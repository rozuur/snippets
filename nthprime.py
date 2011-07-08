"""
A Simple algorithm to find the nth prime number
"""

def prime_sieve(n):
    """
    Using Sieve of Erathosthenes,
    returns primes which are less than n
    """
    nsqrt = int(n ** 0.5) + 1 
    odd_composites = set(odd_comp
                         for odd in xrange(3, nsqrt , 2) 
                         for odd_comp in xrange(odd * odd, n, 2 * odd))
    return [2] + [n for n in xrange(3, n, 2) if n not in odd_composites]

def count(start, step):
    """
    returns a generator for arithmetic progression
    """
    n = start
    while True:
        yield n
        n += step

def isprime(n):
    return not any(n % p == 0 for p in _primes)

def prime_at(index):
    """
    returns at position 'index', assumes zero based indexing
    """
    if(index < len(_primes)):
        return _primes[index]
    last = _primes[-1]
    for i in count(last, 2):
        if isprime(i):
            _primes.append(i)
            if index < len(_primes):
                return _primes[-1]

_primes = prime_sieve(10) # all the primes generated so far 

if __name__ == "__main__":
    for n in xrange(10):
        print 'Prime at %d is %d' % (n, prime_at(n))
    n = input('Using zero indexing enter a number(n) to find n-th prime = ')
    print 'Prime at %d is %d' % (n, prime_at(n))
