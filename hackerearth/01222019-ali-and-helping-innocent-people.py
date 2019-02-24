# Hint 1. To get the line that contains a string, you can use the following code:
S = input()

# Hint 2. This problem has lots of special rules, making it a little difficult to use a for-loop. 
# Also, the length of a string is always 9. 
# So, I'd just use a simple if-else logic, and print 'invalid' or 'valid' depending on a logic.

















# My solution:
S = input() # Get input

if S[2] in 'AEIOUY': # Vowels
    print('invalid')
elif (((int(S[0]) + int(S[1])) & 1 == 1) or
    ((int(S[3]) + int(S[4])) & 1 == 1) or
    ((int(S[4]) + int(S[5])) & 1 == 1) or
    ((int(S[7]) + int(S[8])) & 1 == 1)):
    print('invalid')
else:
    print('valid')
