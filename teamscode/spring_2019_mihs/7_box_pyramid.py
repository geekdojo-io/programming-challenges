def solve(N, k):
    ar = [0]*N
    ar[0] = N
    for i in range(1, N): # Construct cumulativre sum array
        ar[i] = ar[i-1] + (N - i)
    range_from = 0
    for i in range(N):
        if range_from <= k <= ar[i]:
            return i + 1 # Level found
        range_from = ar[i]
    return -1

def test_simple():
    assert solve(1, 1) == 1
    assert solve(3, 5) == 2
    assert solve(2, 3) == 2
    assert solve(4, 10) == 4
    assert solve(7000, 16978200) == 3121

if __name__ == '__main__':
    test_simple()
