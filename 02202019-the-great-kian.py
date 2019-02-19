# Problem: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-great-kian/



# Hint: The problem is to calculate the arithmtic sequence where a step is 3. For example, a1 = ar[0] + ar[3] + ar[6] + ... , 
        a2 = ar[1] + ar[4] + ar[7] + ..., and a3 = ar[2] + ar[5] + ar[8] + ...
        
















# My solution:

N = int(input())
ar = list(map(int, input().split()))
res = [0, 0, 0]
for i in range(3):
    for j in range(i, N, 3):
        res[i] += ar[j]
print('{} {} {}'.format(res[0], res[1], res[2]))
