# python3

import sys
from collections import namedtuple

# create a namedtuple instance: namedtuple(tuple_name, field_names)
# example: namedtuple('user', 'name age id')
Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # segments = [Segment(start=1, end=3), Segment(start=2, end=4), ...]
    points = []
    # advanced sort: sort by "start" asc, if has the same "start", then sort by "end" asc
    ordered_segments = sorted(segments, key=lambda x: (x[0], x[1]))

    # start index far from the leftmost point of all segments
    index = ordered_segments[0][0] - 99999
    for seg in ordered_segments:
        if seg[0] > index:
            points.append(seg[1])
            index = seg[1]
        elif seg[1] < index:
            points[-1] = seg[1]
            index = seg[1]
        continue

    return points

''' unit-test
data = [1,5,2,3,4,5,6,9,7,11,8,10]
segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
p = optimal_points(segments)
print(p)
'''


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
