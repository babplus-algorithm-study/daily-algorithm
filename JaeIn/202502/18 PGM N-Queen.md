```python
def dfsQueen(board,row,n):
    count = 0
    if n == row:
        return 1
    for col in range(n) :
        board[row] = col
        for i in range(row):
            if board[i] == board[row]:
                break
            if abs(board[i]-board[row]) == row - i:
                break
        else :
            count += dfsQueen(board,row+1,n)
    return count

def solution(n):
    answer = dfsQueen([0]*n,0,n)
    return answer

```
