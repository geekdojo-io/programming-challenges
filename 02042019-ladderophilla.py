# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/ladderophilia/


# Hint1: Input contains integer N. So, you can capture the input in the following way:
N = int(input())


# Hint2: Using a pencil and paper, draw a ladder as shown in the sample output of the question
#        and write steps to draw a ladder.





























# My solution:
N = int(input())
for _ in range(N):
    print('*   *')
    print('*   *')
    print('*****')
if N > 0:
    print('*   *')
    print('*   *')
