```python
from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


queue = deque([(x, y, d)])
visited[x][y] = True
count = 1

def bfs():
    global count
    while queue:
        x, y, d = queue.popleft()
        cleaned = False

        for i in range(4):
            nd = (d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, nd))
                count += 1
                cleaned = True
                break

            d = nd

        if not cleaned:
            back_d = (d + 2) % 4
            bx = x + dx[back_d]
            by = y + dy[back_d]

            if 0 <= bx < n and 0 <= by < m and board[bx][by] == 0:
                queue.append((bx, by, d))
            else:
                break

bfs()

print(count)

```
