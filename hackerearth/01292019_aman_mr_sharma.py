# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/aman-mrsharma/

# Hint1: To get the first line which is a number and the rest of lines each contain r and x, 
# you may use the following code like below:
d = int(input())
for _ in range(d):
  r, x = map(int, input().split())
  # your logic goes here
  
# Hint2: to track a total number of toffees, you will need to create a variable (I'll call it 'cnt') outside the for-loop
# and increment the value of cnt when a condition meets.
cnt = 0
for _ in range(d):
  r, x = map(int, input().split())
    # if condition meets, increment cnt
    #   cnt += 1

# Hint3: The distance that Aman ran around a circle of a radius r is:
pie = 22/7
distance1 = pie * 2 * r

# Hint4: Aman is capable of running 100*m meters, which is translated to:
distance2 = 100 * x

# Hint5: Based on the problem, Aman can get a toffee if:
if distance1 <= distance:
  cnt += 1


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  
  

# My solution:

d = int(input())
pie=22/7
cnt = 0
for _ in range(d):
    r, x = map(int, input().split())
    if pie * 2 * r <= 100 * x:
        cnt += 1
print(cnt)
