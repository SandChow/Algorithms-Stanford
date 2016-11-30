from Heap import MinHeap

def isMinHeap(heap, length):
    for i in xrange(1, ((length-2)/2)+1):
        parent = heap[i]
        leftChild = heap[2*i]
        rightChild = heap[2*i+1]
        if leftChild < parent:
            return False
        if rightChild < parent:
            return False
    return True

if __name__=="__main__":
    testHeap = MinHeap()
    testHeap.heapify([10,9,8,7,6,5,4,3,2,1,0,-1,0,1,2,3,4,5,6,7,8,9,10])
    print testHeap.heap
    print isMinHeap(testHeap.heap, testHeap.size)
