class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def heapify(self, data):
        self.size = len(data)
        