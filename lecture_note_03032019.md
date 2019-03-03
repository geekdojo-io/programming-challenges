# Lecture Note for Programming Competition

## More python stuff

### For loop revisited

#### Prefer enumerator over range
Example: Let's say you need to write a code to get sum of numbers when the index of array is even.

Input:

[20, 10, 30, 40, 50]

Output:

100

Explanation:

20, 30 and 50 have the even index becasue index of 20 is 0, 30 is 2 and 50 is 4.

##### Approach 1 - Using `range`
```python
ar = [20, 10, 30, 40, 50]
total = 0
for i in range(len(ar)):
    if i % 2 == 0:
        total += ar[i]
print(total)
```

##### Approach 2 - Using `enumerate`
```python
ar = [20, 10, 30, 40, 50]
total = 0
for i, num in enumerate(ar):
    if i % 2 == 0:
        total += num
print(total)
```

Which would you choose? Go with `enumerate`.

---

Another example: Let's say you need to display items with position.

Input:

['A', 'B', 'C', 'D']

Output:
```
1:A
2:B
3:C
4:D
```

If you use `range`, the code would look like this:

```python
ar = ['A', 'B', 'C', 'D']
for i in range(len(ar)):
    print('{}: {}'.format(i+1, ar[i]))

```

If you asssign a starting index `enumerate`, the code is simpler:

```python
ar = ['A', 'B', 'C', 'D']
for i, item in emumerate(ar, 1):
    print('{}:{}'.format(i, item))
```


### print

Example: Print the items

Input

ar = [10, 20, 30, 40]

Output

10 20 30 40

Answer: Use `print(a, end=' ')`.

```python
for num in ar: # Note how the for loop is used here.
    print(num, end=' ') # Use end=' ' so that print does not create a line break
```

---

### Error handling

https://docs.python.org/3/tutorial/errors.html


Handling reading from Online Judge


```python
def divide(a, b):
    if b == 0:
        raise Exception('divisor cannot be zero')
    return a / b

def solve(a, b):
    try:
        ans = divide(a, b)
        print('Answer is {}'.format(ans))
    except:
        print('An error occurred')

```


```python

while True:
    try:
        line = input()
        # Do something
    except EOFError:
        break
```




### Test (UnitTest)

The [unittest](https://docs.python.org/3/library/unittest.html) is quite cumbersome to use. For convenience, let's use [pytest](https://docs.pytest.org/en/latest/).

First step is to install.
```bash
$ pip install pytest
```

Example: 
```python
def add(a, b):
    return a + b

def test_simple():
    assert add(2, 3) == 5
```

## Math stuff

### Congruence - Modular arthimatics

```
a ≡ b (mod n)
```

Example:

A car is in `a` degrees. Find a final angle after a car turns to left or right for `b` degrees.

```python
def rotate(a, b):
    return (a + b) % 360
```

Anoter example:

A circular list

```python
idx = 27
ar = [1, 2, 3, 4, 5, 6]
items = ar[idx % len(ar)]

```

## Practice

- UVa 11172 - Relational Operators
- UVa 01124 - Celebrity Jeopardy
- UVa 10550 - Combination Lock
- UVa 00272 - TEXT Quotes
