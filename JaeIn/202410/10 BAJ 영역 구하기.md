```python
from collections import deque

N , M , K = map(int , input().split())
board = [list(map(int , input().split())) for _ in range(K)]
visited = [[False] * N for _ in range(M)]
result = []
dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , 1 , -1]

for i in board:
    lx , ly , rx , ry = i
    for x in range(lx , rx):
        for y in range(ly , ry):
            visited[x][y] = True


def bfs(x , y, count):
    queue = deque()
    queue.append([x , y])
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx , ny])
                    count += 1
    return 1 if count == 0 else count

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            n = bfs(i , j , 0)
            result.append(n)

result.sort()
print(len(result))
print(' '.join(map(str , result)))
```
