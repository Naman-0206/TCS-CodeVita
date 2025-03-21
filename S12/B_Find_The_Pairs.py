from collections import defaultdict
import math
from itertools import combinations

def max_distance_pairs(vertices):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    max_dist = 0
    pairs = []

    for v1, v2 in combinations(vertices, 2):
        dist = distance(v1, v2)
        if dist > max_dist:
            max_dist = dist
            pairs = [(v1, v2)]
        elif dist == max_dist:
            pairs.append((v1, v2))

    return pairs

def min_dist(x1, y1, x2, y2, x3, y3):
    numerator = ((y2 - y1) * x3 - (x2 - x1) * y3 + x2 * y1 - y2 * x1)
    
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    
    distance = numerator / denominator
    return distance

def get_all_dist(v11, v12, v21, v22, shape):
    res = []
    for x, y in shape:
        res.append(min_dist(v11, v12, v21, v22, x, y))

    return sorted(res)

n = int(input())
shapes = []
for _ in range(n):
    k = int(input())
    shape = []
    for _ in range(k):
        x, y = map(int, input().split())
        shape.append((x, y))
    shapes.append(shape)

d = defaultdict(list)
for id, shape in enumerate(shapes):
    pairs = max_distance_pairs(shape)
    for (v11,v12), (v21, v22) in pairs:
        d[id].append(get_all_dist(v11, v12, v21, v22, shape))

