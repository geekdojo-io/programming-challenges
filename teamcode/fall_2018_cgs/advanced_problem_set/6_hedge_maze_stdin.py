


# My solution:

def solve(n, ar):
    # Cound the number of consecutive hedges vertically
    res = [0]*n

    for col in range(n):
        prev = ar[0][col]
        cnt = 1 if prev == 'X' else 0
        for row in range(1, n): # Travel vergically
            cur = ar[row][col]
            if cur == 'X' and prev != 'X':
                cnt += 1
            prev = cur
        res[col] = cnt

    return min(res)

for _ in range(int(input())):
    n = int(input())
    ar = []
    for _ in range(n):
        ar.append(input())
    print(solve(n, ar))
