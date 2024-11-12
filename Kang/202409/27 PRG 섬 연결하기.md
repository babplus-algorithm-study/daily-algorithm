```python
from heapq import *
def solution(n, costs):
    for i in range(len(costs)):
        costs[i] = [costs[i][2], costs[i][0], costs[i][1]]
    visit = [True for _ in range(n)]
    if len(costs) == 1:
        return 0
    count = 2
    heapify(costs)
    S, a, b = heappop(costs)
    visit[a] = False
    visit[b] = False
    answer = S

    while count < n:
        stack = []
        signal = True
        while signal:
            S, a, b = heappop(costs)
            if visit[a] and visit[b] == False:
                signal = False        
                count += 1
                answer += S
                visit[a] = False
            elif  visit[b] and visit[a] == False:
                signal = False
                count += 1
                answer += S
                visit[b] = False
            if signal:
                stack.append([S, a, b])
        while stack:
            heappush(costs, stack.pop())

    return answer
```