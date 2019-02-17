# Hint1
# To find a consecutive character, how about creating a variable 'prev'?
# Also, how about creating a variable 'cnt' to track the count of consencutive letters?
# Initially, 'prev' will be set to the first character of the given string.

S = input() # Capture the input
prev = S[0]
cnt = 1


# Hint2
# Then, the for-loop will start from index 1, and compare the current character with the previous character.
# If 'prev' and current character is same, just increment the counter ('cnt'). Otherwise, reset the 'prev' to
# the current character, and also reset 'cnt' to 1.

for i in range(len(S)):
    cur = S[i]
    if cur == prev:
        cnt += 1
    else: # If cur and prev are different, reset counter
        prev = cur
        cnt = 1
        












# My solution:

S = input()
cnt = 1
prev = S[0]
sorry = False
for i in range(len(S)):
    cur = S[i]
    if cur == prev:
        cnt += 1
    else: # If cur and prev are different, reset counter
        prev = cur
        cnt = 1
    if cnt >= 6:
        sorry = True
        break

if sorry:
    print('Sorry, sorry!')
else:
    print('Good luck!')
