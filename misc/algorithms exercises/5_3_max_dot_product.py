# python3

import sys

def max_dot_product(a, b):
    a.sort()
    b.sort()
    product = 0
    for i in range(len(a)):
        product += a[i] * b[i]
    return product

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
