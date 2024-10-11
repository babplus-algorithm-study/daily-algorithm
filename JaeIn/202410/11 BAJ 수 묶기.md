```python
from collections import deque

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

minus = deque()
plus = deque()
zeros = 0
result = 0

for num in arr:
    if num < 0:
        minus.append(num)
    elif num > 1:
        plus.append(num)
    elif num == 0:
        zeros += 1
    else:
        result += num

while len(minus) > 1:
    result += minus.popleft() * minus.popleft()

if minus:
    if zeros > 0:
        result += minus.popleft() * 0
    else:
        result += minus.popleft()

while len(plus) > 1:
    result += plus.pop() * plus.pop()

if plus:
    result += plus.pop()

print(result)

```
