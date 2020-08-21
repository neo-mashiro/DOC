# Uses python3
import sys
import numpy as np

def optimal_weight(items, W):
    """
    input:  items = [(v1, w1), (v2, w2), ...], the k-th item has value "vk" and weight "wk",
            W = capacity of the knapsack
    output: the optimal subset of items, and the maximum value of that set
    time:   O(n*W)
    """
    n = len(items)
    A = np.zeros((W + 1, n + 1), dtype=int)

    for w in range(1, W + 1):
        for i in range(1, n + 1):
            item_i = items[i - 1]  # i-th item (1-indexed)
            v_i, w_i = item_i[0], item_i[1]

            if w - w_i < 0:  # i-th item overweight
                A[w, i] = A[w, i - 1]
            elif A[w, i - 1] >= A[w - w_i, i - 1] + v_i:  # item_i not in S
                A[w, i] = A[w, i - 1]
            else:  # item_i in S
                A[w, i] = A[w - w_i, i - 1] + v_i

    return A[W, n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    w = [(wt, wt) for wt in w]
    print(optimal_weight(w, W))
