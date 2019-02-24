# Problem: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/gas-stations-1/
# Hint1: To capture the first line of input N, X and the second line that contains N space-separate integers, P, 
         you can use the following code:
         
N, X = map(int, input().split())
ar = map(int, input().split())         


# Hint2: Count the number of iterations until X becomes 0 or less.

















# My solution:

N, X = map(int, input().split())
ar = map(int, input().split())
cnt = 0
for num in ar:
    X -= num
    cnt += 1
    if X < 0:
        break
print(cnt)

