# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

# Hint
# To accept L, N and N lines each contain two space saparated integers W and H,
# use the following code.
L = int(input())
N = int(input())
for i in range(N):
    W, H = map(int, input().split())
    #TODO: Implement the logic here (if, else, print, etc.)
	
	
	
	
	
	
	
	
	
	
	
	
	
# My solution
L = int(input())
N = int(input())
for _ in range(N):
    W, H = map(int, input().split())
    if W < L or H < L:
        print('UPLOAD ANOTHER')
    elif W == H:
        print('ACCEPTED')
    else:
        print('CROP IT')
