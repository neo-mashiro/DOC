# python3

import sys, threading
import numpy as np

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().strip().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def _min(self, i):
        if i not in self.mins:
            self.mins[i] = min(self._min(self.left[i]), self.key[i], self._min(self.right[i]))
        return self.mins[i]

    def _max(self, i):
        if i not in self.maxs:
            self.maxs[i] = max(self._max(self.left[i]), self.key[i], self._max(self.right[i]))
        return self.maxs[i]

    def is_bst(self):
        self.valid = True
        self.mins = {-1:np.inf}
        self.maxs = {-1:-np.inf}

        for i in range(self.n):
            if not (self._max(self.left[i]) < self.key[i] < self._min(self.right[i])):
                self.valid = False
        return self.valid

def main():
    T = Tree()
    if T.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
