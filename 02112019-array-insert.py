# Problem: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-insert/

# Hint: You can use the following code to capture input

N, Q = map(int, input().split())
ar = list(map(int, input().split()))
for _ in range(Q):
    op, a, b = map(int, input().split())
    # Write your custom logic. If op == 1, update. If op == 2, print.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# My solution:

N, Q = map(int, input().split())
ar = list(map(int, input().split()))
for _ in range(Q):
    op, a, b = map(int, input().split())
    if op == 1:
        ar[a] = b
    elif op == 2:
        print(sum(ar[a:b+1]))
