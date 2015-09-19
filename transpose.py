#This function will transpose a matrix

def transpose(Matrix):
    '''This takes a list of lists (Matrix), and returns the transposed matrix'''
    transposedMatrix = list(zip(*Matrix))
    return transposedMatrix

