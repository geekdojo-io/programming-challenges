# Question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

# Hint 1
# First line of input will consist of a single integer T 
# denoting number of test-cases. Each test-case consists 
# of a single integer N denoting the seat-number. This is
# translated to the following code:
T = int(input())
for _ in range(T):
    N = int(input())
	# Write code
	
# Hint 2
# There doesn't seem to be a consistant logic about seating
# assignments. So, instead of building a complex logic, why
# don't you create an array that contains the seat number
# and the seat type facing them? Here is an example:
seats = ['', '12 WS', '11 MS', '10 AS', '9 AS', '8 MS', '7 WS', '6 WS', '5 MS', '4 AS', '3 AS', '2 MS', '1 WS', '24 WS',
         '23 MS', '22 AS', '21 AS', '20 MS', '19 WS', '18 WS', '17 MS', '16 AS', '15 AS', '14 MS', '13 WS', '36 WS',
         '35 MS', '34 AS', '33 AS', '32 MS', '31 WS', '30 WS', '29 MS', '28 AS', '27 AS', '26 MS', '25 WS', '48 WS',
         '47 MS', '46 AS', '45 AS', '44 MS', '43 WS', '42 WS', '41 MS', '40 AS', '39 AS', '38 MS', '37 WS', '60 WS',
         '59 MS', '58 AS', '57 AS', '56 MS', '55 WS', '54 WS', '53 MS', '52 AS', '51 AS', '50 MS', '49 WS', '72 WS',
         '71 MS', '70 AS', '69 AS', '68 MS', '67 WS', '66 WS', '65 MS', '64 AS', '63 AS', '62 MS', '61 WS', '84 WS',
         '83 MS', '82 AS', '81 AS', '80 MS', '79 WS', '78 WS', '77 MS', '76 AS', '75 AS', '74 MS', '73 WS', '96 WS',
         '95 MS', '94 AS', '93 AS', '92 MS', '91 WS', '90 WS', '89 MS', '88 AS', '87 AS', '86 MS', '85 WS', '108 WS',
         '107 MS', '106 AS', '105 AS', '104 MS', '103 WS', '102 WS', '101 MS', '100 AS', '99 AS', '98 MS', '97 WS']

# Hint 3 -- Now, all you have to do is to use the above array. For example,
print(seats[1]) # This will print '12 WS'
print(seat[2]) # This will print '11 WS'


















# My solution:

seats = ['', '12 WS', '11 MS', '10 AS', '9 AS', '8 MS', '7 WS', '6 WS', '5 MS', '4 AS', '3 AS', '2 MS', '1 WS', '24 WS',
         '23 MS', '22 AS', '21 AS', '20 MS', '19 WS', '18 WS', '17 MS', '16 AS', '15 AS', '14 MS', '13 WS', '36 WS',
         '35 MS', '34 AS', '33 AS', '32 MS', '31 WS', '30 WS', '29 MS', '28 AS', '27 AS', '26 MS', '25 WS', '48 WS',
         '47 MS', '46 AS', '45 AS', '44 MS', '43 WS', '42 WS', '41 MS', '40 AS', '39 AS', '38 MS', '37 WS', '60 WS',
         '59 MS', '58 AS', '57 AS', '56 MS', '55 WS', '54 WS', '53 MS', '52 AS', '51 AS', '50 MS', '49 WS', '72 WS',
         '71 MS', '70 AS', '69 AS', '68 MS', '67 WS', '66 WS', '65 MS', '64 AS', '63 AS', '62 MS', '61 WS', '84 WS',
         '83 MS', '82 AS', '81 AS', '80 MS', '79 WS', '78 WS', '77 MS', '76 AS', '75 AS', '74 MS', '73 WS', '96 WS',
         '95 MS', '94 AS', '93 AS', '92 MS', '91 WS', '90 WS', '89 MS', '88 AS', '87 AS', '86 MS', '85 WS', '108 WS',
         '107 MS', '106 AS', '105 AS', '104 MS', '103 WS', '102 WS', '101 MS', '100 AS', '99 AS', '98 MS', '97 WS']

T = int(input())
for _ in range(T):
    N = int(input())
    print(seats[N])
