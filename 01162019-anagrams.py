# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

# Hint
# To accep test case T and two strings a and b for each test case, 
# you can use the following code:
T = int(input())
for _ in range(T):
	a = input()
	b = input()
	# TODO: Write code
	
# Hint2: Two strings are anagram if both strings have the same
# count of letters. So, you may create an array that is big
# enough to hold all letters, and count the frequency of letters.
    freq1, freq2 = [0]*256, [0]*256
    for c in a:
        freq1[ord(c)] += 1
    for c in b:
        freq2[ord(c)] += 1
		
# Hint3: To determine the minimum number of character deletion,
# you can simply count the difference of frequencies between
# freq1 and freq2.
    cnt = 0
    for i in range(256):
        cnt += abs(freq1[i] - freq2[i])
# Hint4: Now, you have an answer which is cnt. 
	print(cnt)
	
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# My solution:
T = int(input())
for _ in range(T):
    a = input()
    b = input()
    freq1, freq2 = [0]*256, [0]*256
    for c in a:
        freq1[ord(c)] += 1
    for c in b:
        freq2[ord(c)] += 1
    cnt = 0
    for i in range(256):
        cnt += abs(freq1[i] - freq2[i])
    print(cnt)
