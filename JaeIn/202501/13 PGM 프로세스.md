```python
from collections import deque

def solution(priorities, location):
    answer = []
    dq = deque([(i , p) for i , p in enumerate(priorities)])

    print(dq)

    while len(dq):
        item = dq.popleft()
        if dq and any(item[1] < q[1] for q in dq):
            dq.append(item)
        else:
            answer.append(item)

    for i , q in enumerate(answer):
        if q[0] == location: return i + 1
```
