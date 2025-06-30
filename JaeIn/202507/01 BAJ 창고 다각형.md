```python
N = int(input())

graph = [0] * 1001

max_x = 0
max_y = 0
for i in range(N):
    x , y = map(int , input().split())
    max_x = max(max_x , x)
    max_y = max(max_y , y)
    graph[x] = y


front_prefix = [0] * (max_x + 2)
back_prefix = [0] * (max_x + 2)

max_point = []
h = 0
for i in range(1 , max_x + 3):
    if graph[i] == max_y:
        max_point.append(i)
        break

    h = max(graph[i] , h)
    front_prefix[i + 1] = front_prefix[i] + h


h = 0
for i in range(max_x , 0,  -1):
    if graph[i] == max_y:
        max_point.append(i)
        break

    h = max(graph[i] , h)
    back_prefix[i] = back_prefix[i+1] + h

answer = max(front_prefix) + max(back_prefix)
answer += (max_point[1] - max_point[0] + 1) * max_y

print(answer)
```
