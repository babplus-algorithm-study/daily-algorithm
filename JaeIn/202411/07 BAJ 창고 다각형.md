```python
N = int(input())
graph = [0] * 1001

x_list = []
y_list = []
for i in range(N):
    x, y = map(int, input().split())
    graph[x] = y
    x_list.append(x)
    y_list.append(y)

max_x = max(x_list)
max_y = max(y_list)
prefix = [0] * (max_x + 2)
suffix = [0] * (max_x + 2)

max_point = []
h = 0

for f in range(1, max_x + 3):
    if graph[f] == max_y:
        max_point.append(f)
        break
    h = max(graph[f], h)
    prefix[f] = prefix[f - 1] + h

h = 0
for f in range(max_x, 0, -1):
    if graph[f] == max_y:
        max_point.append(f)
        break
    h = max(graph[f], h)
    suffix[f] = suffix[f + 1] + h

answer = max(prefix) + max(suffix)
answer += (max_point[1] - max_point[0] + 1) * max_y
print(answer)

```
