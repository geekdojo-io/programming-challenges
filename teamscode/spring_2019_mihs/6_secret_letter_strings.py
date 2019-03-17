def solve(s):
    prev, cnt = '', 0
    res = ''
    for c in s:
        if prev == c:
            cnt += 1
        elif c in 'abcd':
            if cnt > 1:
                res += (prev * (cnt - 1))
            prev = c
            cnt = 1
        else:
            prev = ''
            cnt = 0
            res += ' ' if c == '.' else c
    return res


def test_simple():
    assert solve('cdmcy.cbfaacdvdocritabeb.apbiebc.is.baacbdpdbpcacale') == \
        'my favorite pie is apple'
    assert solve('computer.science.rocks') == 'omputer siene roks'
    assert solve('bmbaabtbhb.bibsb.bfbubnb') == 'math is fun'
    assert solve('abscunabflodcawear.seaeddcabsbcdbcdbcd') == 'sunflower seeds'

if __name__ == '__main__':
    test_simple()
