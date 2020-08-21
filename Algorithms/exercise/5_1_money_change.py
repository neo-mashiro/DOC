# python3

import sys

def get_change(m):
    # coins with denominations 1, 5, and 10
    q10, r10 = int(m / 10), (m % 10)
    q5, r5 = int(r10 / 5), (r10 % 5)
    q1 = r5
    
    return q10 + q5 + q1


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
