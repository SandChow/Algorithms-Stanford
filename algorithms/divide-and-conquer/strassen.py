import numpy as np

def strassen(A, B):
    # ensure A and B are both square (n x n) matrices!
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    n = len(A)
    if len(A) is 1:
        return multiply_matrix(A, B) 

    m = n / 2

    # matrix A
    a = [[A[row][column] for column in xrange(m)] for row in xrange(m)]
    b = [[A[row][column] for column in xrange(m, n)] for row in xrange(m)]    
    c = [[A[row][column] for column in xrange(m)] for row in xrange(m, n)]
    d = [[A[row][column] for column in xrange(m, n)] for row in xrange(m, n)]

    # matrix B
    e = [[B[row][column] for column in xrange(m)] for row in xrange(m)]
    f = [[B[row][column] for column in xrange(m, n)] for row in xrange(m)]    
    g = [[B[row][column] for column in xrange(m)] for row in xrange(m, n)]
    h = [[B[row][column] for column in xrange(m, n)] for row in xrange(m, n)]

    # Use the strassen matrix multiplication formulas these values.
    P1 = strassen(a, subtract_matrix(f, h))
    P2 = strassen(add_matrix(a, b), h)
    P3 = strassen(add_matrix(c, d), e)
    P4 = strassen(d, subtract_matrix(g, e))
    P5 = strassen(add_matrix(a, d), add_matrix(e, h))
    P6 = strassen(subtract_matrix(b, d), add_matrix(g, h))
    P7 = strassen(subtract_matrix(a, c), add_matrix(e, f))

    result = [[0 for column in xrange(n)] for row in xrange(n)]

    # i = P4 + P5 - P2 + P6
    i = add_matrix(subtract_matrix(add_matrix(P4, P5), P2), P6)
    # j = P1 + P2
    j = add_matrix(P1, P2)
    # k = P3 + P4
    k = add_matrix(P3, P4)
    # l = P1 + P5 - P3 - P7
    l = subtract_matrix(subtract_matrix(add_matrix(P1, P5), P3), P7)
    
    # m added at various indexes to induce index-shift
    for row in xrange(m):
        for column in xrange(m):
            result[row][column] = i[row][column]
            result[row][column+m] = j[row][column]
            result[row+m][column] = k[row][column]
            result[row+m][column+m] = l[row][column] 
    return result            

# A + B
def add_matrix(A, B):
    n = len(A)
    result = [[0 for column in xrange(n)] for row in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

# A - B
def subtract_matrix(A, B):
    n = len(A)
    result = [[0 for column in xrange(n)] for row in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            result[i][j] = A[i][j] - B[i][j]
    return result

# A x B
def multiply_matrix(A, B):
    n = len(A)
    result = [[0 for column in xrange(n)] for row in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                result[i][j] += A[i][k] * B[k][j] 
    return result


if __name__=="__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    """
                      |19 | 22|
    A*B should output |-------|    
                      |43 | 50|
    """
    print strassen(A, B)
