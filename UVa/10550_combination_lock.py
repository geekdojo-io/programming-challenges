def solve(a, b, c, d):
    def get_degree(x, y):
        return ((x - y) % 40) * 9
    return 1080 + get_degree(a, b) + get_degree(c, b) + get_degree(c, d)

def test_simple():
    assert solve(0, 30, 0, 30) == 1350
    assert solve(5, 35, 5, 35) == 1350
    assert solve(0, 20, 0, 20) == 1620
    assert solve(7, 27, 7, 27) == 1620
    assert solve(0, 10, 0, 10) == 1890
    assert solve(9, 19, 9, 19) == 1890


if __name__ == '__main__':
    while True:
        s = input().strip()
        if s == '0 0 0 0': 
            break
        a, b, c, d = map(int, s.split())
        print(solve(a, b, c, d))
