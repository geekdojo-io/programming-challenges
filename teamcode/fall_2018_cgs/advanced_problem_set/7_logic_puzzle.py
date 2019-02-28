# Problem: 7. Logic Puzzle (190) - https://teamscode.com/assets/docs/fall_2018_cgs/advanced_problem_set.pdf



from collections import defaultdict

students = ['Xis scored higher than Eno',
'Ent scored higher than Vife',
'Neves scored higher than Rouf',
'Thige scored higher than Owt',
'Vife scored higher than Reeth',
'Enin scored higher than Owt',
'Eno scored higher than Neves',
'Thige scored higher than Rouf',
'Eno scored higher than Vife',
'Ent scored the same as Owt',
'Neves scored the same as Enin']

# Build set of dictionaries that hold the comparison data
hi, lo, same = defaultdict(list), defaultdict(list), defaultdict(list)
for s in students:
    tmp = s.split()
    if len(tmp) == 5 and tmp[2] == 'higher': # Higher
        s1, s2 = tmp[0], tmp[-1]
        hi[s1].append(s2) # s1 is higher than s2
        lo[s2].append(s1) # On the flip side, s2 is lower than s1
    elif len(tmp) == 6 and tmp[3] == 'same': # Same
        s1, s2 = tmp[0], tmp[-1]
        same[s1].append(s2)

# Depth first search
def dfs(g, a, b):
    nodes = g[a]
    if len(nodes) == 0:
        return False
    
    res = False
    for s in nodes:
        if b == s or b in same[s]:
            return True
        res |= dfs(g, s, b)
    return res

def solve(a, b):
    # Find same
    if b in same[a] or a in same[b]:
        return  '=' 

    if dfs(hi, a, b): # Graph search to find in the higher score
        return a

    if dfs(lo, a, b): # Graph search to find in the lower score
        return b       

    return '?'

for _ in range(int(input())):
    a, b = input().split()
    print(solve(a, b))
