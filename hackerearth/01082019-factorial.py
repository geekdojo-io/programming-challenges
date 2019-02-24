# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

# Hint 1: How to get the number N as an input?
N = int(input())
# Hint 2: What is factorial of N? It is N * (N-1) * (N-2) * ... * 1
# which is the same as 1 * 2 * ... * (N-1) * N















# My solution:
N = int(input())
res = 1
for num in range(1, N+1):
    res *= num
print(res)
