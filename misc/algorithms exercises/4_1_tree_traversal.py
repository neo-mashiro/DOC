# python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        self.result = []
        self._in_order(0)
        return self.result

    def _in_order(self, idx):
        if idx == -1:
            return
        self._in_order(self.left[idx])
        self.result.append(self.key[idx])
        self._in_order(self.right[idx])

    def pre_order(self):
        self.result = []
        self._pre_order(0)
        return self.result

    def _pre_order(self, idx):
        if idx == -1:
            return
        self.result.append(self.key[idx])
        self._pre_order(self.left[idx])
        self._pre_order(self.right[idx])

    def post_order(self):
        self.result = []
        self._post_order(0)
        return self.result

    def _post_order(self, idx):
        if idx == -1:
            return
        self._post_order(self.left[idx])
        self._post_order(self.right[idx])
        self.result.append(self.key[idx])

def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
