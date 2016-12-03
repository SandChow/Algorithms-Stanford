class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def heapify(self, data):
        self.size = len(data)
        self.heap = [0] + data
        for i in xrange((self.size)/2, 0, -1):
            self.percolateDown(i)

    def extractMin(self):
        assert (len(self.heap) > 1),"Heap is empty!"
        tmp = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolateDown(1)
        self.size -= 1
        return tmp

    def percolateDown(self, parent):
        while (parent * 2) <= self.size:
            smallestChild = self.getSmallestChild(parent)
            if self.heap[parent] > self.heap[smallestChild]:
                self.swap(parent, smallestChild)
            parent = smallestChild

    def getSmallestChild(self, parent):
        # check to see if parent has two children.
        if 2 * parent + 1 > self.size:
            return 2 * parent 
        return 2 * parent if self.heap[2*parent] < self.heap[2*parent+1] else 2 * parent + 1

    def swap(self, a, b):
        tmp = self.heap[b]
        self.heap[b] = self.heap[a]
        self.heap[a] = tmp

    def isEmpty(self):
        if len(self.heap) == 1:
            return True
        return False