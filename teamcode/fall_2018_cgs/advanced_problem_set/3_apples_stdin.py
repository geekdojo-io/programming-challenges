


# My solution:

import math

for _ in range(int(input())):
    n = int(input())
    res = 0
    for _ in range(n):
        box_ar = input().split()
        brand, a = box_ar[0], int(box_ar[1])
        res += math.ceil(a/10)
    print(res)
