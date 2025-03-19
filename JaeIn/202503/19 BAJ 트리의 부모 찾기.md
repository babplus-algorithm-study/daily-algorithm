```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a , b = map(int , input().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(N+1)
def dfs(node ,prev):

    par[node] = prev

    for nxt in graph[node]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            dfs(nxt , node)

dfs(1 , 0)

for p in range(2 , len(par)):
    print(par[p])

```
