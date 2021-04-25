# python3
import sys, threading
from collections import deque

def compute_height_brute_force(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

class Tree:
    ''' a sample class to refresh your memories about a tree data structure '''
    def __init__(self, value, children=[]):
        self._value = value
        self._children = children  # a list of subtrees (recursive)

    def __str__(self):
        ans = "["
        ans += str(self._value)

        for child in self._children:
             ans += ", "
             ans += str(child)
        return ans + "]"

    @property
    def value(self):
        return self._value

    def children(self):
        for child in self._children:
            yield child

    def height(self):
        height = 1
        for child in self._children:
            height = max(height, child.height() + 1)
        return height

def compute_height_recursive(n, parents):
    ''' this function only works for trees of medium size(number of nodes) such as 2,000,
        when applied on trees with more than 100,000 nodes, it definitely fails.
        To handle large inputs, recursion is always a very bad idea, even the memoization cannot save you.
        Whenever you expect the input data to be very huge, please find an alternative algorithm.
    '''
    X = {}  # height for each subtree, for memoization

    def build_tree_height(node):
        if node not in X:
            if node not in parents:  # a leaf
                X[node] = 1
                return X[node]

            children = []
            for node_id, node_parent in enumerate(parents):
                if node_parent == node:
                    if node_id not in X:
                        X[node_id] = build_tree_height(node_id)
                    children.append(X[node_id])
            X[node] = max(children) + 1
        return X[node]

    for node in range(n):
        if parents[node] == -1:
            root = node
        X[node] = build_tree_height(node)

    return X[root]

def compute_height_BFS(n, parents):
    ''' In fact, trees are just a special form of undirected/directed graphs, depends on how you model it.
        all the graph algorithms you've learned can always be slightly modified and then applied on trees.
        for instance, to compute the height/depth of a tree, it's pretty much similar to computing the
        total number of layers for the breadth-first search algorithm to fully traverse a graph.

        Here we'll replace the tree recursion with a BFS traversal, since BFS has linear running time.
        To apply the BFS, we need to build a tree graph and avoid any recursion, so don't use Class Tree().
    '''
    G = {}  # represent the tree graph by adjacency lists {parent:[children], ...}
    for child, parent in enumerate(parents):
        if child not in G:
            G[child] = []
        if parent == -1:
            root = child
        if parent not in G:
            G[parent] = [child]
        else:
            G[parent].append(child)

    Q = deque([root])
    layer = {root:1}
    while Q:
        node = Q.popleft()
        for child in G[node]:
            layer[child] = layer[node] + 1
            Q.append(child)

    # print("G:", G)          # for debugging
    # print("layer:", layer)  # for debugging
    return max(layer.values())

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_BFS(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
