# Problem: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/batman-and-tick-tack-toe/

# Hint 1: You can use the following code to capture the input:

T = int(input())
for _ in range(T):
    board = []
    for _ in range(4):
        board.append(input())
    # TODO: Write custom logic here
    
    
# Hint 2: Batman will win if he can make three 'x's in a row either horizontally, vertically or diagonally.
          So, you will need to handle those cases.





















# My solution

def canWin(row, col, board):
    # .xx
    if col < 2 and board[row][col+1] == 'x' and board[row][col+2] == 'x':
        return True
    # x.x
    if col > 0 and col < 3 and board[row][col-1] == 'x' and board[row][col+1] == 'x':
        return True
    # xx.
    if col >= 2 and board[row][col-1] == 'x' and board[row][col-2] == 'x':
        return True
    # diagonal where . is at the middle
    if col > 0 and col < 3 and row > 0 and row < 3 and \
        ((board[row-1][col-1] == 'x' and board[row+1][col+1] == 'x') or \
         (board[row-1][col+1] == 'x' and board[row+1][col-1] == 'x')):
         return True

    # diagonal: . is at the bottom -> right
    if col < 2 and row >= 2 and \
        (board[row-1][col+1] == 'x' and board[row-2][col+2] == 'x'):
         return True

    # diagonal: . is at the bottom -> left
    if col >= 2 and row >= 2 and \
        (board[row-1][col-1] == 'x' and board[row-2][col-2] == 'x'):
         return True

    # diagonal: . is at the top -> right
    if col < 2 and row < 2 and \
        (board[row+1][col+1] == 'x' and board[row+2][col+2] == 'x'):
         return True

    # diagonal: . is at the top -> left
    if col >= 2 and row < 2 and \
        (board[row+1][col-1] == 'x' and board[row+2][col-2] == 'x'):
         return True

    # .
    # x
    # x
    if row < 2 and board[row+1][col] == 'x' and board[row+2][col] == 'x':
        return True
    # x
    # .
    # x
    if row > 0 and row < 3 and board[row-1][col] == 'x' and board[row+1][col] == 'x':
        return True

    # x
    # x
    # .
    if row >= 2 and board[row-1][col] == 'x' and board[row-2][col] == 'x':
        return True

    return False

def solve(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == '.' and \
                canWin(row, col, board):
                    return True
    return False

T = int(input())
for _ in range(T):
    board = []
    for _ in range(4):
        board.append(input())
    print('YES' if solve(board) == True else 'NO')
