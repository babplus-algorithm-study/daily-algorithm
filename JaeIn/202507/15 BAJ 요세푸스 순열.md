```python
from collections import deque

N , K = map(int, input().split())

persons = [i + 1 for i in range(N)]
answer = []

q = deque()
for p in persons:
    q.append(p)


count = 0
while len(q) > 0:
    count += 1
    items = q.popleft()

    if count % K != 0:
        q.append(items)
    else:
        answer.append(items)

print(f"<{", ".join(map(str, answer))}>")
```
