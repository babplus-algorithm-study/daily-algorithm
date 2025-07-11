```python

N, M, x, y, K = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0]  # [위, 북, 동, 남, 서, 바닥]
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

def dicing(d_index):
    # dice = [위, 북, 동, 남, 서, 바닥]
    top, north, east, south, west, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if d_index == 1:  # 동쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = east, north, bottom, south, top, west
    elif d_index == 2:  # 서쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = west, north, top, south, bottom, east
    elif d_index == 3:  # 북쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = north, bottom, east, top, west, south
    elif d_index == 4:  # 남쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = south, top, east, bottom, west, north

# 방향 배열: 동(1), 서(2), 북(3), 남(4)
dx = [0, 0, 0, -1, 1]  # 인덱스 0은 사용하지 않음
dy = [0, 1, -1, 0, 0]  # 인덱스 0은 사용하지 않음

for d_idx in directions:
    nx = x + dx[d_idx]
    ny = y + dy[d_idx]

    # 범위 체크
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    # 좌표 업데이트
    x, y = nx, ny

    # 주사위 굴리기
    dicing(d_idx)

    # 지도와 주사위 바닥면 상호작용
    if mp[x][y] == 0:
        mp[x][y] = dice[5]
    else:
        dice[5] = mp[x][y]
        mp[x][y] = 0

    print(dice[0])
```
