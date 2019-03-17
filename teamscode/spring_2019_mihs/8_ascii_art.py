def solve(ar):
    M = [' '] * 57

    # Build the character map
    for i in range(ord('A'), ord('Z')+1):
        idx = 1 + (i - ord('A'))*2
        M[idx] = chr(i)
    for i in range(ord('a'), ord('z')+1):
        idx = 2 + (i - ord('a'))*2
        M[idx] = chr(i)        
    M[53], M[54], M[55], M[56] = ' ', '.', ':', '*'

    res = ''
    for s in ar:
        tmp = list(map(int, s.split()))
        for num in tmp:
            res += M[num]
        res += '\n' # New line
    return res

ar = ['53 53 54 38 38 37 38 38 54 53 54 38 38 37 38 38 54',
    '54 38 37 37 37 30 30 37 37 54 37 37 30 30 37 37 37 38 54',
    '54 38 37 30 30 30 30 30 30 30 30 30 30 30 30 30 37 38 54',
    '54 38 37 53 17 53 23 30 44 10 53 49 30 42 53 53 37 38 54',
    '53 53 54 38 37 30 30 30 30 30 30 30 30 30 37 38 54',
    '53 53 53 53 53 54 38 37 30 30 30 37 38 54',
    '53 53 53 53 53 53 53 53 54 38 54'
]

ans = solve(ar)
print(ans)
