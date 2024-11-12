```python
from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False for _ in range(n + 1)]
answer = [[] for _ in range(n + 1)]


def bfs(graph , v , visited):
    queue = deque([v])

    while len(queue) > 0:
        cur = queue.popleft()
        visited[cur] = True

        for i in graph[cur]:
            if not visited[i]:
                answer[i] = cur
                queue.append(i)
                visited[i] = True


bfs(graph , 1 , visited)

for i in range(2 , len(answer)):
    print(answer[i])


```
