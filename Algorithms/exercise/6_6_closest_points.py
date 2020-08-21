#Uses python3
import sys
import math
import numpy as np

def distance(p1, p2):
    """ Calculate the distance between 2 points in 2-D space. """
    x_diff = p1[0] - p2[0]
    y_diff = p1[1] - p2[1]
    return np.sqrt(x_diff ** 2 + y_diff ** 2)

from itertools import combinations

def closetpair_brute_force_2(points):
    min_dist = np.inf
    for (p1, p2) in combinations(points, 2):
        dist = distance(p1, p2)
        if dist < min_dist:
            min_dist = dist
            min_pair = (p1, p2)
    return (min_dist, min_pair)

def closest_pair_in_strip(points_m, bandwidth):
    """
    input: a set of points in the strip, sorted by y coordinates
    output: a tuple(the closest distance, the closest pair) in the strip
    runtime: O(n)
    """
    n = len(points_m)

    # corner case
    if n <= 1:
        return (np.inf, None)
    elif n < 35:
        return closetpair_brute_force_2(points_m)

    # init
    min_m = bandwidth
    pair_m = None

    # iterate through points_m, from bottom to top
    for i in range(len(points_m)):  # O(n) runtime

        # find 7 neighbors
        lower_bound = i + 1
        upper_bound = min(len(points_m), i + 8)  # avoid list index out of range

        for j in range(lower_bound, upper_bound):  # O(1) runtime with finite range
            dist = distance(points_m[i], points_m[j])
            if dist < bandwidth:
                # update min distance, closet pair
                min_m = dist
                pair_m = (points_m[i], points_m[j])

    return (min_m, pair_m)

def divide_conquer(points_x, points_y):
    """
    input: a set of points sorted by x_coordinates and y_coordinates
    output: a tuple(the closest distance, the closest pair)
    """
    n = len(points_x)
    mid = n // 2

    # base case
    if n <= 1:
        return (np.inf, None)
    elif n < 35:
        return closetpair_brute_force_2(points_x)

    # in Python, True = 1, False = 0
    # find the median of x coordinates
    if n % 2:
        center = points_x[mid][0]
    else:
        center = (points_x[mid - 1][0] + points_x[mid][0]) / 2

    # divide into left/right halves sorted by x
    Lx = [p for p in points_x if p[0] <= center]
    Rx = [p for p in points_x if p[0] > center]

    # divide into left/right halves sorted by y
    Ly = [p for p in points_y if p[0] <= center]
    Ry = [p for p in points_y if p[0] > center]

    # make recursive calls on each half
    (min_l, pair_l) = divide_conquer(Lx, Ly)
    (min_r, pair_r) = divide_conquer(Rx, Ry)

    # filter points in the middle strip, find min distance
    bandwidth = min(min_l, min_r)
    points_m = [p for p in points_y if (center - bandwidth) <= p[0] <= (center + bandwidth)]
    (min_m, pair_m) = closest_pair_in_strip(points_m, bandwidth)

    # return the min distance among the 3
    if min_m < bandwidth:
        return (min_m, pair_m)
    elif min_l < min_r:
        return (min_l, pair_l)
    else:
        return (min_r, pair_r)

def closest_pair(points):
    """
    input: a list of points represented by tuples (x_coordinate, y_coordinate)
    output: a tuple(the closest distance, the closest pair)
    runtime: O(nlog(n))
    """
    # sort only once, keep the sorted copy
    points_x = sorted(points, key=lambda p: p[0])  # sort by x_coordinates
    points_y = sorted(points, key=lambda p: p[1])  # sort by y_coordinates

    return divide_conquer(points_x, points_y)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    print("{0:.9f}".format(closest_pair(points)[0]))
