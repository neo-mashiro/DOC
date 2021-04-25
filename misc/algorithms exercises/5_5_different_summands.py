# python3

import sys

def sigma_sum(n):
    if n == 1:
        return 1
    return (1 + n) * n / 2

def optimal_summands(n):
    if n < 3:
        return [n]
    elif n == 3:
        return [1, 2]
    for i in range(1, n):
        if sigma_sum(i) > n:
            k = i - 1
            r = n - sigma_sum(k)
            break

    arr = [(i + 1) for i in range(k)]
    arr[-1] += int(r)
    return arr


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
