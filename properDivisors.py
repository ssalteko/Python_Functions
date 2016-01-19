def divisors(n):
    f = 3
    B = [1]
    if n%2==0:
        B += [2]
        n /= 2
    while n**(1/2)>1:
        if n%f ==0:
            n/=f
            B += [f]
        else:
            f+=2
            
    return divisors
