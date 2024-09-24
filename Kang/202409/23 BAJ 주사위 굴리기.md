```python
import sys
input = sys.stdin.readline

N, M, y, x, K = map(int, input().rstrip().split())
m = [list(map(int, input().rstrip().split())) for _ in range(N)]
orders = list(map(int, input().rstrip().split()))

dice = [[0] * 3 for _ in range(3)]
tmp = 0

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

def check(i):
    global x, y, N, M
    if 0 <= x + dx[i] < M\
    and 0 <= y + dy[i] < N:
        x += dx[i]
        y += dy[i]
        return True
    return False

def is_zero():
    global x, y, N, M

    if m[y][x] == 0:
        return True
    return False

for i in orders:
    if check(i):
        if i == 1: # 동
            tt = tmp
            tmp = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = dice[1][0]
            dice[1][0] = tt
        elif i == 2: # 서
            tt = tmp
            tmp = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = dice[1][2]
            dice[1][2] = tt
        elif i == 3: # 북
            tt = tmp
            tmp = dice[0][1]
            dice[0][1] = dice[1][1]
            dice[1][1] = dice[2][1]
            dice[2][1] = tt
        else: # 남
            tt = tmp
            tmp = dice[2][1]
            dice[2][1] = dice[1][1]
            dice[1][1] = dice[0][1]
            dice[0][1] = tt
        
        if is_zero():
            m[y][x] = tmp
        else:
            tmp = m[y][x]
            m[y][x] = 0
        
        print(dice[1][1])
```