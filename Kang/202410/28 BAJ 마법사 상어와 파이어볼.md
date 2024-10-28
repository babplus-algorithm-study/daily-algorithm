```python
import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
fireball = []

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

graph = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    (graph[y - 1][x - 1]).append((m, s, d))

def set_mess(f_list):
    mess = 0
    for m, _, _ in f_list:
        mess += m
    return mess // 5

def set_direction(f_list):
    first_direction = f_list[0][2] % 2
    for i in range(1, len(f_list)):
        if first_direction != (f_list[i][2] % 2):
            return (1, 3, 5, 7)
    
    return (0, 2, 4, 6)

def set_velocity(f_list):
    count = len(f_list) 
    vel = 0
    for _, s, _ in f_list:
        vel += s
    return vel // count

def set_new_graph(n_g, fire):
    global N
    y, x, m, s, d = fire
    pdx = dx[d] * (s % N)
    pdy = dy[d] * (s % N)
    px = x + pdx
    py = y + pdy

    if px < 0:
        px = N + px 
    elif px >= N:
        px = px - N
    if py < 0:
        py = N + py
    elif py >= N:
        py = py - N

    n_g[py][px].append((m, s, d))

def move_fire(k):
    global graph, N, K
    if k == K:
        answer = 0
        for y in range(N):
            for x in range(N):
                for m, _, _ in graph[y][x]:
                    answer += m
        return answer
    new_graph = [[[] for _ in range(N)] for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            for (m, s, d) in graph[y][x]:
                if m != 0:
                    set_new_graph(new_graph, (y, x, m, s, d))
    for y in range(N):
        for x in range(N):
            if len(new_graph[y][x]) > 1:
                fire_list = new_graph[y][x]
                mess = set_mess(fire_list)
                d_list = set_direction(fire_list)
                v = set_velocity(fire_list)
                new_graph[y][x] = []
                if mess != 0:
                    for d in d_list:
                        new_graph[y][x].append((mess, v, d))
                    
    graph = new_graph

    return move_fire(k + 1)

print(move_fire(0))
```