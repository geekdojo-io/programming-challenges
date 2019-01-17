# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

# Hint:
# Palindrome is a string that reads the same backward as forward,
# e.g., madam, or abcdcba.






















# My Solution
def isPalindrome(s):
    n = len(S)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

S = input()
print('YES' if isPalindrome(S) else 'NO')
