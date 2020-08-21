# python3

'''calculate the sum of last digits of a Fibonacci numbers array'''
import sys

def fib_last_digit(n):
    pattern = '011235831459437077415617853819099875279651673033695493257291'
    ptn_len = len(pattern)
    m = n % ptn_len
    return int(pattern[m])

def fib_sum_last_digit(n):
    assert n >= 0, "Invalid input!"
    m = n % 60
    total = 0
    for i in range(m + 1):
        total += fib_last_digit(i)
    return total % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_last_digit(n))
