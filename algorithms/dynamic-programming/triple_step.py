def recursive(n):
    """ Causes stack overflow for large values of n. """

    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return recursive(n-1) + recursive(n-2) + recursive(n-3)

def iterative(n):
    sol = [0, 1, 2, 4] + [0] * (n-1)
    for i in xrange(4, n+1):
        sol[i] = sol[i - 1] + sol[i - 2] + sol[i - 3];
    return sol[n]

if __name__=="__main__":
   print recursive(5)
   print iterative(5)
