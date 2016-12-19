# String matching using Knuth-Morris-Pratt

def KMP(string, pattern):
    if pattern is not "":
        lps = [0] * (len(pattern) + 1)
        lps[0] = -1
        k = -1 # k refers to the number of matched elements so far

        # pattern is pre-processed using the algorithm
        for i in xrange(1, len(pattern)+1):
            while k > -1 and pattern[k] is not pattern[i-1]:
                k = lps[k]
            k += 1
            lps[i] = k

        k = 0
        pattern_matches = 0
        beginning_indexes = []

        # actual pattern matching starts here
        for i in xrange(len(string)):
            while(k > -1 and pattern[k] != string[i]):
                k = lps[k]
            k += 1
            if k is len(pattern):
                pattern_matches += 1
                beginning_indexes.append(i - k + 1)
                k = lps[k]

        return pattern_matches, beginning_indexes

if __name__ == '__main__':
    print KMP("ABC ABCDAB ABCDABCDABDE", "ABCDAB")
    print KMP("AAAAAAA", "AAA")