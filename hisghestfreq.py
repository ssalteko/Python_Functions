def highestfreq(n):
    '''returns a dictionary consisting of keys that are in each dictionary, and their highest frequency'''
    dictr = {}
    for x in n:
        for p,b in x.items():
            #print(p,b)
            if p not in dictr:
                dictr[p] = 1
            if dictr[p]<b:
                dictr[p] = b
    return dictr
