# Uses python3
import sys
import itertools
import numpy as np

def partition3_brute_force(arr):
    for c in itertools.product(range(3), repeat=len(arr)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(arr[k] for k in range(len(arr)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

def partition3_knapsack(arr):  # (Max time used: 0.25/10.00, max memory used: 18698240/536870912.)
    """ This problem can be seen as a variant of the knapsack problem,
        we only need to call knapsack() twice, then check if both output == int(sum(arr) / 3).
        However, our stress_test() discovers one pitfall in this algorithm, that is, when we call
        knapsack(souvenirs, W), souvenirs must be reversely sorted! In some cases, there are a lot
        of ways to put items in the knapsack with size = (sum(arr) / 3), even if the 1st call works,
        the 2nd call might fail. For example, if souvenirs = [1,1,1,2,2,2], then the 3 knapsacks
        should all be [1,2] respectively. But if you get a knapsack [1,1,1] in the first call,
        there's no way to get another knapsack of size 3 with the remaining souvenirs [2,2,2].
    """
    def knapsack(souvenirs, W):
        n = len(souvenirs)
        A = np.zeros((W + 1, n + 1), dtype=int)
        S = []

        souvenirs.sort(reverse=True)  # CAVEAT! must sort first!
        for w in range(1, W + 1):
            for i in range(1, n + 1):
                w_i = souvenirs[i - 1]  # i-th item (1-indexed)

                if w - w_i < 0:  # i-th item overweight
                    A[w, i] = A[w, i - 1]
                elif A[w, i - 1] >= A[w - w_i, i - 1] + w_i:  # w_i not in knapsack
                    A[w, i] = A[w, i - 1]
                else:  # w_i in knapsack
                    A[w, i] = A[w - w_i, i - 1] + w_i

        row, col = W, n
        while A[row, col] > 0:
            w = souvenirs[col - 1]
            c1 = A[row, col - 1]  # case1: inherited from the left position, last souvenir not in knapsack
            if row < w:  # overweight
                c2 = 0
            else:
                c2 = A[row - w, col - 1] + w  # case2: derived by adding last souvenir to knapsack

            if c1 >= c2:
                col -= 1
            else:
                S.append(col)  # 1-base-indexed souvenir
                souvenirs.pop(col - 1)
                row -= w
                col -= 1

        return A[W, n], souvenirs

    if sum(arr) % 3 != 0:
        return 0
    else:
        partition_size = int(sum(arr) / 3)

    partition1, remains1 = knapsack(arr, partition_size)
    if partition1 != partition_size:
        return 0

    partition2, remains2 = knapsack(remains1, partition_size)
    if partition2 != partition_size:
        return 0
    else:
        return 1

def partition3_direct_dp(arr):  # (Max time used: 0.16/10.00, max memory used: 19165184/536870912.)
    """
    In order to equally partition the souvenirs into 3 bags, each bag must have size = sum(arr) / 3,
    since the input are all integers, the partition size must be integers rather than float numbers.
    Let A be a 3-dimensional array, A[k][size1][size2] means that given the first k numbers in arr,
    whether we can partition in a way that the 1st bag has size1 and the 2nd bag has size2,
    so the idea is to compute by recurrence the value of A[k][size1][size2], which returns True/False.

    By dp induction, the last number is either in bag1, or bag2, or not in these 2 bags,
    let num = arr[k-1], which is the k-th number in arr, and so we have:
    A[k][size1][size2] = A[k-1][size1 - num][size2] | A[k-1][size1][size2 - num] | A[k-1][size1][size2]

    At the end, we just need to return A[len(arr)][sum(arr) / 3][sum(arr) / 3], either True or False.
    However, this algorithm is more time-consuming and space-consuming, since the size of A is cubic.
    """
    if sum(arr) % 3 != 0:
        return 0
    else:
        partition_size = int(sum(arr) / 3)

    # 2-step initialize
    A = {1:{}}
    for size1 in range(partition_size + 1):
        A[1][size1] = {}
        for size2 in range(partition_size + 1):
            A[1][size1][size2] = False

    A[1][arr[0]][0] = True
    A[1][0][arr[0]] = True

    # recurrence computation
    for k in range(2, len(arr) + 1):
        A[k] = {}

        for size1 in range(partition_size + 1):
            A[k][size1] = {}

            for size2 in range(partition_size + 1):
                num = arr[k - 1]

                case1 = (size1 >= num) and A[k - 1][size1 - num][size2]
                case2 = (size2 >= num) and A[k - 1][size1][size2 - num]
                case3 = A[k - 1][size1][size2]

                A[k][size1][size2] = case1 | case2 | case3  # "or" relationship

    return (1 if A[len(arr)][partition_size][partition_size] else 0)

def stress_test(n, func):
    for _ in range(n):
        arr = list(np.random.randint(1, 100, 10))
        print(arr)
        if partition3_brute_force(arr) != func(arr):
            print("error found!")
            break
    return


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))

    # stress_test(100, partition3_knapsack)
    # stress_test(100, partition3_direct_dp)
    # print(partition3_knapsack(A))
    print(partition3_direct_dp(A))
