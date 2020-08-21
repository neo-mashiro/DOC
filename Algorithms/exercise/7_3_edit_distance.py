# Uses python3
import numpy as np

def edit_distance(str1, str2):

    m, n = len(str1), len(str2)
    A = np.zeros((m + 1, n + 1), dtype=int)  # minimum penalty matrix
    S1, S2 = str(), str()

    # 0. base case
    A[:,0] = np.dot(range(m + 1), 1)
    A[0,:] = np.dot(range(n + 1), 1)

    # 1. by recurrence, find the minimum penalty at each (row, col) position
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            case1 = A[i - 1, j - 1] + (1 if str1[i - 1] != str2[j - 1] else 0)
            case2 = A[i - 1, j] + 1
            case3 = A[i, j - 1] + 1

            A[i, j] = min(case1, case2, case3)

    # 2. trace back the matrix from the lower right corner to reconstruct the optimal alignment
    #    if "case1" == "case2 or case3", it's a tie, a gap insertion is preferred.
    i, j = m, n
    while i > 0 or j > 0:
        if i == 0:
            S1 = '+' + S1
            S2 = str2[j - 1] + S2
            j -= 1
            continue
        elif j == 0:
            S1 = str1[i - 1] + S1
            S2 = '+' + S2
            i -= 1
            continue

        if A[i, j] == A[i - 1, j] + 1:  # case2: match str1[i - 1] with a gap
            S1 = str1[i - 1] + S1
            S2 = '+' + S2
            i -= 1
        elif A[i, j] == A[i, j - 1] + 1:  # case3: match str2[j - 1] with a gap
            S1 = '+' + S1
            S2 = str2[j - 1] + S2
            j -= 1
        else:  # case1: match str1[i - 1] with str2[j - 1]
            S1 = str1[i - 1] + S1
            S2 = str2[j - 1] + S2
            i -= 1
            j -= 1

    # print(S1)
    # print(S2)
    return A[m, n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
