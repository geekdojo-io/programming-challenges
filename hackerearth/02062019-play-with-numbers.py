# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/play-with-numbers-2/

# Hint 1: You can capture the first line, next line and next Q lines in the following way:

N, Q = map(int, input().split())
tmp = list(map(int, input().split()))
# Do something with tmp

for _ in range(Q):
    L, R = map(int, input().split())
    # Do something with L and R
    
    
   
   
# Hint 2: If you solve in a bruteforce way, you will most likely get a time-out error.
#         Can you speed it up using a cumulative sum of an array? https://www.geeksforgeeks.org/python-program-to-find-cumulative-sum-of-a-list/










# Hint 3: Here is an example of how you can build a cumulative sum of an array.

N, Q = map(int, input().split())

# Build an array that contains cumulative sum
tmp = list(map(int, input().split()))
ar = [0]*(N+1)
for i in range(N):
    ar[i+1] = ar[i] + tmp[i]

for _ in range(Q):
    L, R = map(int, input().split())
    # Do something with L and R
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
 
 
 
 # My solution:
 
 N, Q = map(int, input().split())

# Build an array that contains cumulative sum
tmp = list(map(int, input().split()))
ar = [0]*(N+1)
for i in range(N):
    ar[i+1] = ar[i] + tmp[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print((ar[R] - ar[L-1])//(R-L+1))
