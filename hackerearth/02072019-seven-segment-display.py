# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/



# Hint 1: Capture the input for the question, you can use the following approach:

T = int(input())
for _ in range(T):
    S = input()
    # Do something
    
    
    
    
    
    
    
    
    
# Hint 2: There might be multiple ways to solve the problem. One way would be to use a dictionary. https://www.geeksforgeeks.org/python-dictionary/
































# My solution:
def solve(S):
    map_ = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
    
    num = 0
    for c in S:
        num += map_[c]
    res = ''        
    while num > 0:
        if num & 1 == 1:
            res += '7'
            num -= 3
        else:
            res += '1'
            num -= 2
    return res
    
T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
