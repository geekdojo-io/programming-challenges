# Hint 1
# The bruteforce approach is to simply increment a day and track the distance traveled so far.
# Unfortunately, this approach is going to give TLE (Time Limit Exceed) error.
# So, a better algorithm is necessary. How about using a math formula to calculate the 
# number of days that are required to cover the distnace?

days = math.ceil(S / X) # S is the total distance, and X is the distance that can be covered on a regular day.

# Hint 2
# And, it is necessary to capture the exception days with distance, and sort by the days.
# Then, for each exception day in a loop, it can calculate the distance that have been traveled so far
# right before the exception day, and check if the distance traveled so far reached the goal (S).
# If not, the distance traveled so far will need to include the distance for the exception day, and check
# if the distance travled so far reached the goal. 

# Hint 3
# As a last step, it is necessary to handle the case where the distance traveled so far is still smaller than the goal (S) 
# after the loop is completed.




# My solution:

import math

def solve(S, X, N, ar):
    ar.sort()
    if N == 0:
        return math.ceil(S / X)
    cur_day, so_far = 0, 0
    for tup in ar:
        t, y = tup[0], tup[1]
        regular_days = t - cur_day - 1 # Exclude t
        min_days = min(regular_days, math.ceil((S - so_far) / X))
        dist = min_days * X
        cur_day += min_days
        so_far += dist
        
        if so_far >= S:
            return cur_day
        dist += y
        cur_day += 1
        so_far += y # include t
        if so_far >= S:
            return cur_day

    return cur_day + math.ceil((S - so_far) / X)

S, X, N = map(int, input().split())
ar = []
for _ in range(N):
    T, Y = map(int, input().split())
    ar.append((T, Y)) # add tuple (T, Y) to list

print(solve(S, X, N, ar))
