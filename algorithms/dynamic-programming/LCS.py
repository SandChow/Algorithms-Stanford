""" 
Implementation of longest common subsequence (LCS) algorithm.
"""

def lcs(A, B):
    a = len(A)
    b = len(B)
    D = [[0]*(b+1) for i in xrange(a+1)]
    for i in xrange(a+1):
        for j in xrange(b+1):
            if j == 0 or i == 0:
                D[i][j] = 0
            elif A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1] + 1;
            else:
                D[i][j] = max(D[i][j-1], D[i-1][j])
    return D[a][b]

if __name__ == '__main__':
    print lcs("ABCD", "ABDCD")
    print lcs("ABCBDAB", "BDCABCABCBDAB")