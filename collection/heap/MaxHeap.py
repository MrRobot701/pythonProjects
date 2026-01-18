def heapSort(array, size):
    heap = buildMaxHeap(array, size)
    print(heap.heap)
    for i in range(size - 1, 0, -1):
        heap.swap(0, i)
        heap.setSize(heap.size - 1)
        heap.heapify(0)



def right(index):
    return 2 * (index + 1)


def left(index):
    return 2 * index + 1


def parent(index):
    return (index - 1) // 2


def buildMaxHeap(array, size):
    heap = MaxHeap(array, size)
    half = (size >> 1) - 1
    for i in range(half, -1, -1): heap.heapify(i)
    return heap


class MaxHeap:

    def __init__(self, heap, size):
        self.heap = heap
        self.size = size

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def heapify(self, index):
        largest = index
        l = left(index)
        r = right(index)
        if l < self.size and self.heap[largest] < self.heap[l]: largest = l
        if r < self.size and self.heap[largest] < self.heap[r]: largest = r
        if largest != index:
            self.swap(largest, index)
            self.heapify(largest)

    def setSize(self, newSize):
        self.size = newSize
