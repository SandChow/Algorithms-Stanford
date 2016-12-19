# Returns the length of the longest sequence of increasing numbers in an unsorted array.

# Uses Dynamic Programming
def LIS_Num_DP(arr):
    n = len(arr)
    table = [1] * n

    for i in xrange(1, n):
        for j in xrange(0, i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j]+1) 

    return table[n-1]

def binary_search_index(arr, lis, n):
    high = len(lis) - 1
    low = 0
    while high >= low:
        middle = (high + low) / 2
        if middle < (len(lis)-1) and arr[lis[middle]] <= n and n <= arr[lis[middle+1]]:
            return middle + 1
        elif n > arr[lis[middle]]:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def LIS_nlogn(arr):
    lis = [0]
    mapper = [-1] * len(arr)

    for i in xrange(1, len(arr)):
        if arr[i] < arr[lis[0]]:
            lis[0] = i
        elif arr[i] > arr[lis[-1]]:
            lis.append(i)
            mapper[lis[-1]] = lis[-2]
        else:
            index = binary_search_index(arr, lis, arr[i])
            lis[index] = i
            mapper[lis[index]] = lis[index-1]

    index = lis[-1]
    final_lis = []
    while index != -1:
        final_lis = [arr[index]] + final_lis
        index = mapper[index]
    return final_lis

if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print LIS_nlogn(arr)