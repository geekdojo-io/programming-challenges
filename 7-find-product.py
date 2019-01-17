# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

# Hint
# To get the input N and the elements of the array, use the following code:
N = int(input())
ar = list(map(int, input().split()))
# 10^9 + 7 is the same as 1000000007

# This is a fairly straightforward problem. Just code carefully using the logic
# described in the Explanation of the problem.

























# My solution:
N = int(input())
ar = list(map(int, input().split()))
res = 1
for i in range(len(ar)):
    res = (res * ar[i]) % 1000000007
print(res)
