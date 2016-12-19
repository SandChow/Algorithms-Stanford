def sumNoNeighbours(arr):
    n = len(arr)
    table = [0] * n
    table[0] = arr[0]
    table[1] = arr[1]

    for i in xrange(2, n):
        table[i] = max(table[i-1], table[i-2] + arr[i])

    return table[n-1]

def sumNoNeighboursNoSpace(arr):
    withNext = 0
    withoutNext = 0
    for i in arr:
        newWithoutNext = max(withoutNext, withNext)
        withNext = withoutNext + i
        withoutNext = newWithoutNext
    return max(withoutNext, withNext)

if __name__ == '__main__':
    print sumNoNeighbours([10, 12, 15, -1, -1, 100, -1, -1])
    print sumNoNeighbours([5,  5, 10, 40, 50, 35])
    print sumNoNeighboursNoSpace([3, 2, 5, 10, 7])
    print sumNoNeighboursNoSpace([5,  5, 10, 40, 50, 35])
