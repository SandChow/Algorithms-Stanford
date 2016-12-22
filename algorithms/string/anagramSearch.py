NO_OF_CHARS = 256

def search(string, pattern):
    patternCounter = [0] * NO_OF_CHARS
    currentScanCounter = [0] * NO_OF_CHARS
    indexes = []
    pLength = len(pattern)

    for i in xrange(pLength):
        patternCounter[ord(pattern[i])] += 1
        currentScanCounter[ord(string[i])] += 1

    for i in xrange(pLength, len(string)):
        if characterCountCompare(patternCounter, currentScanCounter):
            indexes.append(i - pLength)
        currentScanCounter[ord(string[i-pLength])] -= 1
        currentScanCounter[ord(string[i])] += 1

    if characterCountCompare(patternCounter, currentScanCounter):
        indexes.append(len(string) - pLength)

    return indexes

def characterCountCompare(arr1, arr2):
    for i in xrange(NO_OF_CHARS):
        if arr1[i] != arr2[i]:
            return False
    return True

if __name__ == '__main__':
    print search("BACDGABCDA", "ABCD")