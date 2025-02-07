```python
import copy

def dfs(start, temp, visited):
    visited[start] = True
    count = 1
    for t in temp[start]:
        if not visited[t]:
            count += dfs(t, temp, visited)
    return count

def check(a, b, graph):
    temp = copy.deepcopy(graph)
    temp[a].remove(b)
    temp[b].remove(a)
    arr = []
    visited = [False for _ in range(len(temp))]

    for i in range(1, len(temp)):
        if not visited[i]:
            arr.append(dfs(i, temp, visited))

    return abs(arr[0] - arr[1])

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    result = float('inf')

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        diff = check(a, b, graph)
        result = min(result, diff)

    return result


```
