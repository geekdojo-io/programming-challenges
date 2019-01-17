# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8

# Hint:
# This problem requires you to find the series of prime number
# finding if a single number is prime or not.
# To print output in format like "2 3 5 7" from an array ar = [2, 3, 5, 7], 
# you can use:
print(' '.join(ar))


























# My solution:
import math

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True 

N = int(input())
res = []
for num in range(2, N + 1):
    if isPrime(num):
        res.append(str(num))
print(' '.join(res))
