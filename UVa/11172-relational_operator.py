# Problem: https://uva.onlinejudge.org/index.php?option=onlinejudge&Itemid=99999999&page=show_problem&category=0&problem=2113&mosmsg=Submission+received+with+ID+22892210


# Solution:

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
