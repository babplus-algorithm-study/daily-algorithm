```python
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    max_num = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == "L":
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    max_num = max(max_num, visited[nx][ny])
    return max_num

result = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == "L":
            result = max(result, bfs(x, y))

print(result)
```
