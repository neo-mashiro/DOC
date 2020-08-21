# python3

'''calculate the last digit of a Fibonacci number'''
import sys

def fib_last_digit(n):
    pattern = '011235831459437077415617853819099875279651673033695493257291'
    ptn_len = len(pattern)
    m = n % ptn_len
    return int(pattern[m])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_digit(n))
