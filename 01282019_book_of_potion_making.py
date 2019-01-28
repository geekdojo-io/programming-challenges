# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/
# Hint: To get the 10-digit ISBN code, you can use the following code:
S = input()

# Hint2: If you read the question carefully, you will need to check the length of the ISBN.
if len(S) != 10:
    # handle illegal ISBN

# Hint3: You can convert each letter to integer and multiply with an increasing number within for-loop like this:
total = 0
for i in range(10):
    total += (i+1) * int(S[i])
    
# Hint4: You can check if the sum is divisible by 11:
if total % 11 == 0:
    # handle the case where the sum is divisible by 11.
