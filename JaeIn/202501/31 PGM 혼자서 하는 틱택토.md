```python
def check_winning(board):
    win_O, win_X = 0, 0

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            win_O += 1
        elif board[0][0] == "X":
            win_X += 1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            win_O += 1
        elif board[0][2] == "X":
            win_X += 1

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "O":
                win_O += 1
            elif board[i][0] == "X":
                win_X += 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "O":
                win_O += 1
            elif board[0][i] == "X":
                win_X += 1

    return [win_O, win_X]

def solution(board):
    num_O, num_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                num_O += 1
            elif board[i][j] == "X":
                num_X += 1
    if num_O == 0 and num_X == 0:
        return 1

    win_O, win_X = check_winning(board)

    if win_O and win_X:
        return 0

    if num_O == num_X:
        if win_O >= 1:
            return 0
        else:
            return 1

    if num_O == (num_X + 1):
        if (win_O == 0 and win_X >= 1):
            return 0
        else:
            return 1

    return 0
```
