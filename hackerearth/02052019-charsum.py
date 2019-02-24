# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/char-sum-2d3a6ab5/

# Hint 1: The first and only line of input contains the String S, and so you can capture the input like this:
S = input()

# Hint 2: Use ord() function to convert a letter to an integer. For example, 
#         ord('a') is 97, and ord('b') is 98.




























# My solution:
S = input()
w = 0
for c in S:
    w += ord(c) - ord('a') + 1
print(w)
