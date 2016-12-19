# pattern search in string using finite automata / finite state machine

NO_OF_CHARS = 256

def search(string, pattern):
    table = [[0] * (NO_OF_CHARS) for i in xrange(len(pattern) + 1)]
    computeTruthTable(pattern, table)
    state = 0
    for i in xrange(len(string)):
        state = table[state][ord(string[i])]
        if state is len(pattern):
            print i - len(pattern) + 1

# get next state from current character in pattern
def getNS(pattern, state, character):
    if state < len(pattern) and character == pattern[state]:
        return state + 1
    for ns in xrange(state, 0, -1):
        if pattern[ns-1] == character:
            for i in xrange(ns-1):
                if pattern[i] is not pattern[state-ns+1+i]:
                    break
                if i is ns-1:
                    return ns
    return 0

def computeTruthTable(pattern, table):
    for state in xrange(len(pattern)+1):
        for char in xrange(NO_OF_CHARS):
            table[state][char] = getNS(pattern, state, chr(char))


if __name__ == '__main__':
    print search("ABC ABCDAB ABCDABCDABDE", "ABCDAB")
    # print search("AAAAAAA", "AAA")