def sumprimes(n):
    '''this sums primes below the value n'''
    m = [0] * n
    j = 3
    sumofprimes = 2
    while j < n:
        if m[j] == 0:
            sumofprimes += j
            p = j
            while p < n:
                m[p] = 1
                p += j
        j += 2
    print (sumofprimes)
