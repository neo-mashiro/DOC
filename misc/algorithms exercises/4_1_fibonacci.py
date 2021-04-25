# python3

'''calculate a Fibonacci number'''
import functools

@functools.lru_cache(maxsize=None)  # None: cache size has no upper bound
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
