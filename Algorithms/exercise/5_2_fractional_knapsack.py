# python3

import sys

def get_optimal_value(capacity, weights, values):

    # create a list of item tuples(value, weight, unit_val)
    items = []
    for i in range(len(weights)):
        items.append((values[i], weights[i], values[i] / weights[i]))
        
    # sort by unit_val in descending order
    items.sort(key=lambda x: x[-1], reverse=True)
    
    value = 0
    weight = 0
    
    while weight < capacity and len(items) > 0:
        item = items.pop(0)
        if (weight + item[1]) <= capacity:
            value += item[0]
            weight += item[1]
        else:
            value += item[0] * ((capacity - weight) / item[1])
            weight = capacity
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
