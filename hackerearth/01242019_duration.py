# Hint: To get N as first line with next N lines with SH, SM, EH and EM,
#       you can use the following code:
T = int(input())
for _ in range(T):
    SH, SM, EH, EM = map(int, input().split())
    # Your logic goes here
    
# Hint2 - This problem can be solved as a simple math problem dealing with hours and minutes.














# My solution:

T = int(input())
for _ in range(T):
    SH, SM, EH, EM = map(int, input().split())
    start = SH*60 + SM
    end = EH*60 + EM
    diff = end - start
    print(diff//60, diff % 60)
