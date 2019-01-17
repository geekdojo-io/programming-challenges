# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/

# Hint
# 1. To get N as input, use
N = int(input())
# 2. Use a pencil and paper to go through the provided
# sample explanation, and understand the rule.
# 2. Understand the rule of the game thoroughly. Remember,
# the rule of the game is to print the name of the person
# who puts the last bricks.
# 3. In the sample explanatin, Motu had to put 1 brick instead
# of 6 bricks in round 3. Why? It's because only 1 brick remained.
# So, Motu's bricks can be expressed as the following statement:
total += min(i * 2, N - total)
# 4. Game ends when total == N where total is the number of bricks
# that Patlu and Motu used.

# My solution
N = int(input())
i, sofar = 0, 0
while True:
    i += 1
    sofar += min(i, N - sofar)
    if sofar == N:
        print('Patlu')
        break
    sofar += min(i*2, N - sofar)
    if sofar == N:
        print('Motu')
        break 
