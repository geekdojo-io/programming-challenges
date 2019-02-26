# Hint
# To repeat a string for 'n' times, you can simply multiply string by n. Example:
>>> s = 'XXOX'
>>> s * 2 # Repeat s by 2 times.
XXOXXXOX # Output of s * 2

# My solution:

T = int(input())
for i in range(T):
   h, w, n = map(int, input().split())
   ar = []
   for _ in range(h):
       ar.append(input())
   for _ in range(n):
       for s in ar:
           print(s * n)
