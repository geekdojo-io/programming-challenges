# programming-challenges

## Tips for Programming challenges
1. Don't solve a wrong problem -- Read a question carefully, especially the provided sample inputs and outputs.
2. Attempt to solve a problem with a pencil and paper before starting to type code.
3. Work on concrete examples. Most of the times, a problem is given with a set of sample inputs and outputs. Use them.
4. Test your code before submission. Usually there is a *penalty* for incorrect submissions.
5. Know your language (Python, C++, Java, etc.) well including its libraries.

## Math

### Round off, Round up, Round

```py
>>> import math # import math module
>>> math.floor(13.5) # round off
13
>>> math.ceil(13.5) # round up
14
>>> 10 // 3 # integer division
3
>>> 10 / 3 # floating division
3.3333333333333335
>>> a = 10/3
3.3333333333333335
>>> round(a, 2) # Round to 2 decimals
3.33

```

## Sorting

### Ascending, Descending

```py

>>> ar = [5, 2, 1, 7, 9]
>>> ar = sorted(ar) # Regular sorting (ascending)
>>> ar
[1, 2, 5, 7, 9]
>>> ar = sorted(ar, reverse=True)
>>> ar
[9, 7, 5, 2, 1]


```

## Read Input and Generate Output

### Read from stdin and output to stdout

#### Read from stdin
```py
# Input: The first line contains an integer L. The following L lines will each contain two numbers, N1 and N2

# Example input
3
6 12
1 54
2 2

# Sample code:

L = int(input())
for _ in range(L):
    N1, N2 = map(int, input().split())
    # TODO: Write a custom logic

```

#### Output to stdout

```py

# Example output:
72
55
4

# Sample code 1

ar = ['72', '55', '4']
for num in ar:
    print(num)

# Sample code 2

ar = ['72', '55', '4']
print('\n'.join(ar))

# Sample code 3

ar = [72, 55, 4]
print('\n'.join(str(num) for num in ar))

```

### Read from file and Output to file

#### Read from file

```py
with open('input.txt', 'r') as f:
    lines = f.readlines() # lines is a list of string
```

#### Output to file

```py

# Example output:
72
55
4

ar = ['72', '55', '4']


with write('output.txt', 'r') as f:
    f.write('\n'.join(ar))
```


## Practice

### Golem

Input and Output: Read from stdin and output to stdout.

Sample Problem: You are facing off against a golem. In order to beat it, you must cast a magic spell. You are given two numbers. Your task is to find the largest number possible either by adding or multiplying the two numbers together in order to cast the strongest spell.

Input: The first line contains an integer L. The following L lines will each contain two numbers, N1 and N2.

Output: For each set of two numbers, print the largest number possible through either adding or multiplying the two numbers together.

Example Input:

```
5
6 12
1 54
2 2
9 -17
-7 -7
```

Example Output:

```
72
55
4
-8
49
```

### [Catlin Gabel 2018 Fall Programming Contest](https://teamscode.com/assets/docs/fall_2018_cgs/advanced_problem_set.pdf)
