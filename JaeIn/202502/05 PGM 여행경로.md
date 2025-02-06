```python
from collections import defaultdict
def solution(tickets):
    path = []

    graph = defaultdict(list)
    for s , e in tickets:
        graph[s].append(e)


    for i in graph:
        graph[i].sort()

    start = 'ICN'


    def dfs(start , path , graph):
        while graph[start]:
            next_airport = graph[start].pop(0)
            dfs(next_airport , path , graph)

        path.append(start)

    dfs(start , path , graph)




    return path[::-1]
```
