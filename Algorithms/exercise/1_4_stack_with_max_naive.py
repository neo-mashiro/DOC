#python3
import sys

class StackWithMax:

    def __init__(self):
        self._items = []
        self._max = []

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def push(self, item):
        ''' O(1) run time '''
        self._items.append(item)
        if self._max == []:
            self._max = [item]
        elif item >= self._max[-1]:
            # when equal, must also append, otherwise, pop() will mess up self._max
            # e.g. self._items = [0,1,1,1], self._max = [0,1], after pop(), max is 0.
            self._max.append(item)

    def pop(self):
        ''' O(1) run time '''
        if not self._items:
            raise Exception("Stack underflow!")
        if self._max[-1] == self._items[-1]:
            self._max.pop()
        return self._items.pop()

    def max(self):
        ''' O(1) run time '''
        return self._max[-1] if self._max else None

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
