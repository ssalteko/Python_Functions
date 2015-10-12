def mkstrlist():
    '''takes a users input, and returns a list of those inputs'''
    t = []
    while 1:
        g = str(input("here, "))
        if g == '':
            break
        t.append(g)
        print(t)
    return t

