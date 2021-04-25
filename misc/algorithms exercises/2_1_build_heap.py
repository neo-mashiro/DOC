# python3

from math import floor, log

class MinHeap:
    ''' 0-based indices of nodes, implemented as an array '''
    def __init__(self, keys):
        self._heap = keys
        self._size = len(keys)
        self._swaps = []
        self.heapify()

    def __str__(self):
        return str(self._heap) + "\n" + "size: " + str(self.size)

    @property
    def size(self):
        return self._size

    @staticmethod
    def parent(node):  # no "self" argument for static methods
        return floor(0.5 * (node - 1)) if node > 0 else None

    def l_child(self, node):  # not static, to derive child, must depend on an instance
        return (2 * node + 1) if (2 * node + 1) < self._size else None

    def r_child(self, node):  # any non-root node always has a parent, but not all nodes have children
        return (2 * node + 2) if (2 * node + 2) < self._size else None

    def _siftup(self, node):  # iterative version (recursion also works)
        ''' nothing would happen if the heap property is already maintained '''
        while node > 0 and self._heap[node] < self._heap[MinHeap.parent(node)]:
            parent = MinHeap.parent(node)
            self._heap[node], self._heap[parent] = self._heap[parent], self._heap[node]
            self._swaps.append((node, parent))
            node = parent

    def _siftdown(self, node):  # recursive version (iteration also works)
        ''' nothing would happen if the heap property is already maintained '''
        l, r = self.l_child(node), self.r_child(node)
        min_node, min_key = node, self._heap[node]
        if l and self._heap[l] < min_key:
            min_node, min_key = l, self._heap[l]
        if r and self._heap[r] < min_key:
            min_node, min_key = r, self._heap[r]
        if node != min_node:
            self._heap[node], self._heap[min_node] = self._heap[min_node], self._heap[node]
            self._swaps.append((node, min_node))
            self._siftdown(min_node)

    def heapify(self):
        ''' heapify in-place, no additional space used, takes O(nlogn) time.
            iterate thru nodes 1 by 1 from bottom to top (except the leaves), _siftdown() to repair the heap property.
            this is just a naive implementation, in heapq, the in-place heapify() only takes O(n) linear time.
        '''
        for node in range(self.size - 1, -1, -1):  # from node(n - 1) to node(0)
            self._siftdown(node)

    def extract_min(self):
        if self._size == 0:
            raise Exception("Heap underflow!")
        minimum = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._size -= 1
        if self._size != 0:
            self._siftdown(0)
        return minimum

    def push(self, key):
        self._heap.append(key)
        self._size += 1
        self._siftup(self._size - 1)

    def remove(self, node):
        self._heap[node] = self._heap[-1]
        self._heap.pop()
        self._size -= 1
        self._siftup(node)
        self._siftdown(node)

    def set_key(self, node, key):
        self._heap[node] = key
        self._siftup(node)
        self._siftdown(node)


if __name__ == '__main__':
    n = int(input())
    data = [int(s) for s in input().split()]
    assert n == len(data)
    H = MinHeap(data)
    print(len(H._swaps))
    for swap in H._swaps:
        print(swap[0], swap[1])
