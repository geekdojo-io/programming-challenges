# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

# Hint 1: How to assign 3 integers to l, r, k?
#     First, you need to split an input using input().split().
#     Then, you will want to use map(int, input().split()) to create an iterator.
#     So, the code will look like this:
l, r, k = map(int, input().split())

# Hint 2: determin if num is divisible by k?
if num % k == 0:
    # do something
	
# Solution
l, r, k = map(int, input().split())
cnt = 0
for num in range(l, r+1):
    if num % k == 0:
        cnt += 1
print(cnt)
