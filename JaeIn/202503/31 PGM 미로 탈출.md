```python
from collections import deque

def bfs(start , end , maps):
    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , -1 , 1]

    row , col = len(maps) , len(maps[0])

    for i in range(row):
        for j in range(col):
            if maps[i][j] == start:
                start = [i , j]
            elif maps[i][j] == end:
                end = [i , j]


    q = deque()
    q.append([start[0] , start[1] , 0])
    visited = [[0] * col for _ in range(row)]


    while q:
        x , y , dis = q.popleft()

        if x == end[0] and y == end[1]:
            return dis

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                    q.append([nx , ny , dis + 1])
                    visited[nx][ny] = 1

    return -1

def solution(maps):
    answer = 0

    laber = bfs('S' , 'L' , maps)
    if laber == -1:
        return -1

    exit = bfs('L' , 'E' , maps)
    if exit == -1:
        return -1

    return laber + exit
```
