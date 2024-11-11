```python
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())
graph = [[-1] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = b
    graph[a - 1][b] = b - 1

r_set = []

for y in range(H):
    for x in range(N - 1):
        if graph[y][x] == -1\
        and graph[y][x + 1] == -1:
            r_set.append((x, y))
ll = len(r_set)
p_count = -1
p_signal = False

def check():
    signal = True

    for i in range(N):
        px = i
        py = 0
        while py < H:
            if graph[py][px] != -1:
                px = graph[py][px]
            py += 1
        if px != i:
            signal = False
            break

    return signal

def back(p, idx):
    global p_count, p_signal
    if p == 4:
        return
    
    if check():
        if p_count == -1:
            p_count = p
        else:
            p_count = min(p, p_count)
        return

    for i in range(idx, ll):
        if p_signal:
            break
        x, y = r_set[i]
        if graph[y][x] == -1 and graph[y][x + 1] == -1:
            graph[y][x] = x + 1
            graph[y][x + 1] = x
            back(p + 1, i + 1)
            graph[y][x] = -1
            graph[y][x + 1] = -1

back(0, 0)

print(p_count)
```