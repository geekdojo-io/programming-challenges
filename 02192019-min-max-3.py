# Problem: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/min-max-3/

# Hint1: You can find the min and max by looping through an array and compare each value.
#       Alternative, you can use min() and max() function to find the min and max value.

# Hint2: To find if all numbers are within min and max value, one approach is to use a dictionary to
# .      capture the occurrance of numbers in an array.

# Hint3: Once you capture the occurance of each number, you can loop from the min to max value, and find
# .      if the number between the min and max value appeared. If the number did not appear, you print 'NO'.
#        Otherwise, print 'YES'.






# My solution:

from collections import Counter

def solve(ar):
    min_, max_ = min(ar), max(ar)
    ft = Counter() # Frequency table
    for num in ar:
        ft[num] += 1
    for i in range(min_ + 1, max_ + 1):
        if ft[i] == 0:
            return False
    return True

N = int(input())
ar = list(map(int, input().split()))
print('YES' if solve(ar) else 'NO')
