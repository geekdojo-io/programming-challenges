# programming-challenges

## Tips for Programming challenges
1. Don't solve a wrong problem -- Read a question carefully, especially the provided sample inputs and outputs.
2. Attempt to solve a problem with a pencil and paper before starting to type code.
3. Work on concrete examples. Most of the times, a problem is given with a set of sample inputs and outputs. Use them.
4. Test your code before submission. Usually there is a *penalty* for incorrect submissions.

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