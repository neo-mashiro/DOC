# Uses python3
import sys

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search_recursive(a, x):
    left, right = 0, len(a) - 1
    mid = (left + right) // 2
    # base case
    if len(a) < 10:
        return linear_search(a, x)

    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search_recursive(a[:mid], x)
    else:
        index = binary_search_recursive(a[(mid + 1):], x)
        if index == -1:
            return -1
        else:
            return index + mid + 1

def binary_search(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if x == a[m]:
            return m
        elif x < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
