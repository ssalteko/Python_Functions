def PrimesList(n):
    '''this lists primes below the value n'''
    m = [0] * n
    j = 3
    ListOfPrimes = [2]
    while j < n:
        if m[j] == 0:
            ListOfPrimes += [j]
            p = j
            while p < n:
                m[p] = 1
                p += j
        j += 2
    print (ListOfPrimes)
