```python
from collections import deque

n , m = map(int , input().split())
time = 0
MAX = 100001
visited = [0] * MAX


def bfs(n):
    queue = deque()
    queue.append((n , 0))
    visited[n] = True

    while queue:
        num , time = queue.popleft()
        if num == m:
            return time
        for i in [num * 2 , num - 1 , num + 1]:
           if  0 <= i <= MAX - 1 and not visited[i]:
                queue.append((i , time + 1))
                visited[i] = True

result = bfs(n)
print(result)



```
