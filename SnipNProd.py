def SnipNProd(n,matrix):
    '''Returns the maximum product of n adjacent elements'''

    M = 0
    rows = len(matrix)
    cols = len(matrix[0])
    Tmatrix = tuple(zip(*matrix))
    Rmatrix = []
    for x in matrix:
        Rmatrix += [x[::-1]]
    Rmatrix = tuple(Rmatrix)
    print(Rmatrix)

    if n > rows:
        return False
    if n > cols:
        return False
    #n horizontal
    for x in matrix:
        i = 0
        nn = n
        while i <= len(x)-n:
            t = 0
            m = 1
            while t < n:
                m *= x[i+t]
                t += 1
            if m > M:
                M = m
            i += 1
            nn += 1
    #n vertical
    for x in Tmatrix:
        i = 0
        nn = n
        while i <= len(x)-n:
            t = 0
            m = 1
            while t < n:
                m *= x[i+t]
                t += 1
            if m > M:
                M = m
            i += 1
            nn += 1
    #n diagonal forward
    i = 0
    while i <= rows -n:
        
        j = 0
        while j <= cols -n:
            m = 1
            t = 0
            while t < n:
                m *= matrix[i+t][j+t]
                t +=1
            if m > M:
                M = m
            j += 1
        i += 1
    #n diagonal back
    i = 0
    while i <= rows -n:
        
        j = 0
        while j <= cols -n:
            m = 1
            t = 0
            while t < n:
                m *= Rmatrix[i+t][j+t]
                t +=1
            if m > M:
                M = m
            j += 1
        i += 1
            
    return M
