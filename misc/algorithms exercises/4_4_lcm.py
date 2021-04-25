# python3

'''calculate the least common multiple of 2 integers'''
import sys

def lcm(a, b):
    assert (a >= 1 and b >= 1), "Invalid input"

    s = min(a, b)  # smaller
    l = max(a, b)  # larger

    for multiplier in range(1, s):
        p = l * multiplier
        if (p % s) == 0:
            return p
    return a * b

def EuclidGCD(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return EuclidGCD(b, a_prime)

def EuclidLCM(a, b):
    if a * b == 0:
        return 0
    gcd = EuclidGCD(a, b)
    if gcd == 1:
        return a * b
    else:
        return gcd * EuclidLCM(a/gcd, b/gcd)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
