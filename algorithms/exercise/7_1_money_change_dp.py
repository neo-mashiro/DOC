# Uses python3
import sys
import numpy as np

def get_change_recursive(money):
    """ (Max time used: 0.19/5.00, max memory used: 19492864/536870912.) """
    # denominations 1, 3, 4
    M = {0:0, 1:1, 2:2, 3:1, 4:1, 5:2, 6:2}  # initialize for memoization

    def recurse(amount):
        nonlocal M
        if amount in M:
            return M[amount]
        else:
            M[amount] = np.inf

        for d in [1, 3, 4]:
            if amount >= d:
                num_of_coins = recurse(amount - d) + 1
                if num_of_coins < M[amount]:
                    M[amount] = num_of_coins

        return M[amount]

    return recurse(money)

def get_change_iterative(money):
    """ (Max time used: 0.16/5.00, max memory used: 18632704/536870912.) """
    # denominations 1, 3, 4
    M = {0:0}
    for m in range(1, money + 1):
        M[m] = np.inf
        for d in [1, 3, 4]:
            if m >= d:
                num_of_coins = M[m - d] + 1
                if num_of_coins < M[m]:
                    M[m] = num_of_coins
    return M[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change_recursive(m))
