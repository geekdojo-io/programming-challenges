# Hint
# To repeat a string for 'n' times, you can simply multiply string by n. Example:
>>> s = 'XXOX'
>>> s * 2 # Repeat s by 2 times.
XXOXXXOX # Output of s * 2

# My solution:

for _ in range(int(input())):
   h, w, n = map(int, input().split())
   s = ''
   for _ in range(h):
       s += input()*n + '\n'
   print(s*n)
