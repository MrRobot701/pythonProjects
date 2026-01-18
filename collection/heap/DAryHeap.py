from heapq import heapify


class DAryHeap[T]:

    def __init__(self, d: int, heap: list[T], size: int):
        self.__d = d
        self.__heap = heap
        self.size = size

    def parent(self, i: int) -> int:
        return (i - 1) // self.__d

    def child(self, i, k) -> int:
        return i * self.__d + 1 + k

    def swap(self, i: int, j: int) -> None:
        tmp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = tmp

    def heapify(self, i) -> None:
        largest = i
        for k in range(self.__d):
            child = self.child(i, k)
            if child < self.size and self.__heap[child] > self.__heap[largest]: largest = child
        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)

    def heapifyLoop(self, i) -> None:
        current = self.__heap[i]
        while i < self.numberOfNonLeaves():
            largest = i
            for k in range(self.__d):
                child = self.child(i, k)
                if child < self.size and self.__heap[child] > self.__heap[largest]: largest = child
            if largest != i:
                self.__heap[i] = self.__heap[largest]
                i = largest
            else: break
        self.__heap[i] = current

    def bubbleUp(self, i):
        current = self.__heap[i]
        while i > 0:
            parent = self.parent(i)
            if self.__heap[parent] < self.__heap[i]:
                self.__heap[i] = self.__heap[parent]
                i = parent
            else: break
        self.__heap[i] = current

    def numberOfNonLeaves(self) -> int:
        return (self.size - 1) // self.__d


