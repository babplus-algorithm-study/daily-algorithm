```python
from collections import deque

def solution(maps):
    answer = []

    dx = [1 , -1 , 0 , 0]
    dy = [0 , 0 , 1 , -1]

    row_len = len(maps)
    col_len = len(maps[0])

    visited = [[0] * col_len for _ in range(row_len)]


    def bfs(x , y):
        q = deque()
        q.append((x , y))
        visited[x][y] = 1
        sum_date = int(maps[x][y])

        while q:
            cx , cy = q.popleft()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < row_len and 0 <= ny < col_len and visited[nx][ny] == 0:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = 1
                        q.append((nx , ny))
                        sum_date += int(maps[nx][ny])

        return sum_date

    for r in range(row_len):
        for c in range(col_len):
            if visited[r][c] == 0 and maps[r][c] != 'X':
                answer.append(bfs(r , c))


    answer.sort()
    if len(answer):
        return answer

    return [-1]
```
