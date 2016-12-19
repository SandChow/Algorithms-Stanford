def DP(arr):
    n = len(arr)
    table = [0] * n
    table[0] = arr[0]

    for i in xrange(1, n):
        table[i] = table[i-1] + arr[i]
        if table[i] < 0:
            table[i] = 0

    return max(table)

def Kadane(arr):
    n = len(arr)
    highest, current = arr[0], arr[0]

    for i in arr[1:]:
        current = max(i, current + i)
        highest = max(highest, current)
    return highest
    
if __name__ == '__main__':
    print DP([5, 4, -1, 10])
    print Kadane([5, 4, -1, 10])