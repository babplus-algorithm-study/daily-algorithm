```python
from collections import deque

def solution(board):

    x_l = len(board)
    y_l = len(board[0])

    s_x, s_y = 0 , 0

    dx = [1 , -1 , 0 , 0]
    dy = [0 , 0 , -1 , 1]

    for i in range(x_l):
        for j in range(y_l):
            if board[i][j] == 'R':
                s_x, s_y = i , j

    def bfs():
        q = deque()
        q.append((s_x , s_y))
        visited = [[0] * y_l for _ in range(x_l)]
        visited[s_x][s_y] = 1

        while q:
            x , y = q.popleft()
            if board[x][y] == 'G':
                return visited[x][y]

            for i in range(4):
                nx , ny = x , y
                while True:
                    nx = dx[i] + nx
                    ny = dy[i] + ny

                    if 0 <= nx < x_l and 0 <= ny < y_l and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    elif 0 > nx or nx >= x_l or 0 > ny or ny >= y_l:
                        nx -= dx[i]
                        ny -= dy[i]
                        break

                if 0 <= nx < x_l and 0 <= ny < y_l and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx , ny))

        return -1


    answer = bfs()
    if answer > 0:
        answer -= 1

    return answer
```
