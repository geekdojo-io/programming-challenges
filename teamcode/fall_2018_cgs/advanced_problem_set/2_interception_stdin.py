


# My solution:

import math

def solve(v, d):
    t = d / v
    v2 = d / (t - 1)
    return math.floor(v2) + 1

for _ in range(int(input())):
    v, d = map(int, input().split())
    print(solve(v, d))
