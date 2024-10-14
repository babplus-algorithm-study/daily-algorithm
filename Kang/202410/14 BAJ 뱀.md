```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
game_map = [[0] * N for _ in range(N)] # 빈칸 0, 뱀 1, 사과 2

for _ in range(K):
    y, x = map(int, input().rstrip().split())
    game_map[y - 1][x - 1] = 2

game_map[0][0] = 1
snack = deque([(0, 0)])

L = int(input().rstrip())
lotate = deque([])

for _ in range(L):
    t, l = input().rstrip().split()
    lotate.append((int(t), l))

time = 0

direction = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    time += 1
    
    x, y = snack[0]

    px = x + dx[direction]
    py = y + dy[direction]
    # 벽에 부딪히고 뱀의 몸통이 아닌지 확인
    if 0 <= px < N\
    and 0 <= py < N\
    and game_map[py][px] != 1:
        # 사과가 있는지 확인
        if game_map[py][px] == 2:
            snack.appendleft((px, py))
            game_map[py][px] = 1
        else:
            snack.appendleft((px, py))
            game_map[py][px] = 1
            del_x, del_y = snack.pop()
            game_map[del_y][del_x] = 0
    else:
        break

    # lotate 큐 확인
    if lotate\
    and lotate[0][0] == time:
        t, l = lotate.popleft()
        if l == "D":
            direction += 1
            if direction == 4:
                direction = 0
        else:
            direction -= 1
            if direction == -1:
                direction = 3


print(time)
```