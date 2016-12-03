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
        minimum = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.percolateDown(1)
        return minimum 

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.percolateUp(self.size)


    def percolateDown(self, parent):
        while (parent * 2) <= self.size:
            smallestChild = self.getSmallestChild(parent)
            if self.heap[parent] > self.heap[smallestChild]:
                self.swap(parent, smallestChild)
            parent = smallestChild

    def percolateUp(self, child):
        while child > 1 and self.heap[child] < self.heap[child/2]:
            self.swap(child, child/2)
            child /= 2

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