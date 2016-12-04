from LCS import lcs

def add_for_palindrome_LCS(string):
    LCS = lcs(string, string[::-1])
    return len(string) - LCS

def add_for_palindrome(string):
    n = len(string)
    if n == 0:
        return 0
    D = [[0]*n for i in xrange(n)]

    for i in xrange(n-2, -1, -1):
        for j in xrange(i+1, n):
            if string[i] == string[j]:
                if j-i > 2:
                    D[i][j] = D[i+1][j-1]  
            else:
                D[i][j] = 1
                if j-i > 1:
                    D[i][j] += min(D[i+1][j], D[i][j-1])
    return D[0][n-1]

if __name__ == '__main__':
    print add_for_palindrome_LCS("AB")
    print add_for_palindrome("abcdefg")