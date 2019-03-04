# Problem: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3565

# Comment: This is a simple problem that echos the input as output.
#          The key of this problem is to handle the end of file (or end of input). This can be done by using try/except.

# Solution:

while True:
    try:
        print(input())
    except EOFError:
        break
