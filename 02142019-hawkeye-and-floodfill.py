# Problem: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/hawkeye-and-floodfill/

# Hint1: You can capture the input in the following way:

N = int(input())
i, j, p = map(int, input().split())
# Write custom logic


# Hint2: Think about a math formula to calculate the impact of an arrow on a given position (row and col of the board).
















# My solution:

N = int(input())
i, j, p = map(int, input().split())

for row in range(N):
    for col in range(N):
        dist = max(abs(i-row), abs(j-col))
        impact = max(0, p - dist)
        print(impact, end=' ')
    print('')
