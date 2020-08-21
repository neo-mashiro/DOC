# python3

'''calculate the greatest common divisor of 2 integers'''
import sys

def gcd(a, b):
    assert (a >= 1 and b >= 1), "Invalid input"

    s = min(a, b)  # smaller
    l = max(a, b)  # larger

    for divisor in range(1, s):
        q = s / divisor
        r = s % divisor
        if (r == 0) and (l % q) == 0:
            return int(q)
    return 1

def EuclidGCD(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return EuclidGCD(b, a_prime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(EuclidGCD(a, b))
