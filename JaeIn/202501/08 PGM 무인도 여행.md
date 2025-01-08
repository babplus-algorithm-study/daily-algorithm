```python
import sys

sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []

    len_x = len(maps)
    len_y = len(maps[0])

    visited = [[0 for _ in range(len_y)] for _ in range(len_x)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        food = int(maps[x][y])
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len_x and 0 <= ny < len_y:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    food += dfs(nx, ny)
        return food

    for i in range(len_x):
        for j in range(len_y):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(dfs(i, j))

    return sorted(answer) if len(answer) >= 1 else [-1]

```
