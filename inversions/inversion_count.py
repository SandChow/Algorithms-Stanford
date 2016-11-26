"""
This program counts the number of inversions in an integer array using the basic merge sort concept!

IntegerArray.txt from https://www.coursera.org/learn/algorithms-divide-conquer/exam/YLbzP/programming-assignment-2
outputs 2407905288 inversions.
"""
def count(arr):
    if len(arr) < 2:
        return arr, 0
    left_half, left_count = count(arr[:len(arr)/2]) 
    right_half, right_count = count(arr[len(arr)/2:])
    sorted_array, split_count = merge_and_count(left_half, right_half)
    return sorted_array, left_count + right_count + split_count

def merge_and_count(x, y):
    count = 0
    sorted_array = []
    while len(x)*len(y) is not 0:
        # < or <= can be used in conventional mergesort but not here due to the way we count!
        if x[0] <= y[0]:
            sorted_array.append(x.pop(0))
        else:
            sorted_array.append(y.pop(0))
            # The length of x is added here instead of an increment by 1 because we want
            # to account for all the values in x that are more than the popped y value.
            count += len(x)
    if len(y) is 0:
        sorted_array += x
    else:
        sorted_array += y
    return sorted_array, count

if __name__=="__main__":
    with open("IntegerArray.txt", "r") as input:
        arr = []
        for line in input:
            arr.append(int(line))
    print "total ->",
    """
                     (n*(n+1)) 
    Uses formula --> ---------
                         2
    Not optimized to work with duplicates.
    """
    if all(arr[i] > arr[i+1] for i in xrange(len(arr)-1)):
        print len(arr)*(len(arr)-1)/2
    else:
        print count(arr)[1]
