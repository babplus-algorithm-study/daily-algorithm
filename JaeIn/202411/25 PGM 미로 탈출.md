```python
from collections import deque

def solution(maps):
    answer = 0
    temp1 = 0
    temp2 = 0

    len_x = len(maps)
    len_y = len(maps[0])
    visited = [[0] * len_y for _ in range(len_x)]

    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , -1 , 1]

    sx , sy = 0 , 0
    lx , ly = 0 , 0
    ex , ey = 0 , 0


    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] == 'S':
                sx , sy = i , j
            elif maps[i][j] == 'L':
                lx , ly = i , j
            elif maps[i][j] == 'E':
                ex , ey = i , j


    def bfs_l(x , y):
        queue = deque([(x , y , 0)])
        visited[x][y] = 1

        while queue:
            cx , cy , cnt = queue.popleft()

            if maps[cx][cy] == 'L':
                return cnt

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < len_x and 0 <= ny < len_y and visited[nx][ny] == 0:
                    if maps[nx][ny] != 'X':
                        queue.append((nx , ny , cnt + 1))
                        visited[nx][ny] = 1
        return -1


    def bfs_e(x , y):
        queue = deque([(x , y , 0)])
        visited[x][y] = 1

        while queue:
            cx , cy , cnt = queue.popleft()

            if maps[cx][cy] == 'E':
                return cnt

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < len_x and 0 <= ny < len_y and visited[nx][ny] == 0:
                    if maps[nx][ny] != 'X':
                        queue.append((nx , ny , cnt + 1))
                        visited[nx][ny] = 1
        return -1


    temp1 += bfs_l(sx , sy)
    if temp1 == -1:
        return -1

    visited = [[0] * len_y for _ in range(len_x)]
    temp2 += bfs_e(lx , ly)
    if temp2 == -1:
        return -1

    answer = temp1 + temp2

    return answer
```
