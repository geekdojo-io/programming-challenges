



# My solution:

def get_breaktime(n, ar):
    ar_sum = ar.copy()
    # Calculate cumulative sum
    for i in range(1, n):
        ar_sum[i] += ar_sum[i-1]
    res = 0
    for i in range(n-1):
        res += ar_sum[i] / 10
    return res

def solve(n, ar):
    ar = sorted(ar, reverse=False)
    min_time = get_breaktime(n, ar)
    
    ar = sorted(ar, reverse=True)
    max_time = get_breaktime(n, ar)

    return round(max_time - min_time, 1)

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    print(solve(n, ar))
