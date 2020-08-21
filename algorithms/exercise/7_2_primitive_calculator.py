# Uses python3
import sys
import numpy as np

def optimal_sequence(n):
    # going from 1 to n, with available operations *2, *3, or +1
    M = {1:0}  # minimum number of operations
    O = {1:[]}  # series of operations, e.g. O[n] = [2,3,1] means n = x * 2 * 3 + 1
    sequence = [1]

    for num in range(2, n + 1):
        M[num] = np.inf
        case1, case2, case3 = np.inf, np.inf, np.inf

        if num % 3 == 0:
            case1 = M[num / 3] + 1
        if num % 2 == 0:
            case2 = M[num / 2] + 1
        case3 = M[num - 1] + 1

        M[num] = min(case1, case2, case3)

        if M[num] == case1:
            O[num] = O[num / 3] + [3]
        elif M[num] == case2:
            O[num] = O[num / 2] + [2]
        else:
            O[num] = O[num - 1] + [1]

    last_num = 1
    for operation in O[n]:
        if operation == 1:
            last_num += 1
        elif operation == 2:
            last_num *= 2
        else:
            last_num *= 3
        sequence.append(last_num)

    assert sequence[-1] == n, "check your sequence"
    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
