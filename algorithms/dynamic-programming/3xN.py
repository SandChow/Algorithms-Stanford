""" 
The goal of this program is to fill a 3 x N baord with dominos 
of different sizes like 3x1 and 2x1.

Concept used are derived from: 
http://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf
"""

def domino_3x1(n):
    """
    Basic concept: D(n) = D(n-1) + D(n-3) 
    """

    table = [1, 1, 1] +[0] * (n-2)
    for i in xrange(3, n+1):
        table[i] = table[i-1] + table[i-3]
    return table[i]

def domino_2x1(n):
    """ 
    Basic concept: D(n) = D(n-2) + 2A(n-1)
                   A(n) = D(n-1) +  A(n-2)
    """

    if n == 0:
        return 1

    D = [1, 0] + [0] * (n-1)
    A = [0, 1] + [0] * (n-1)

    for i in xrange(2, n+1):
        D[i] = D[i-2] + 2 * A[i-1]
        print str(i) + ": " + str(D[i])
        A[i] = D[i-1] + A[i-2]

if __name__ == '__main__':
    # print domino_3x1(5)
    domino_2x1(500000)