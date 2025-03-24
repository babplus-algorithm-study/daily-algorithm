```python
# 회전을 여러 번 해야하는 경우가 있으므로 deepcopy를 통해 복사
from copy import deepcopy

T = int(input())
for _ in range(T):
    N, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0] * N for _ in range(N)]

    if d < 0:
        # 반시계방향
        # -45: 360+45로 처리하면 동일함
        d += 360

    if d == 360 or d == 0:
        for i in board:
            print(*i)

    else:
        for _ in range(d // 45):
            mid = N//2

            for i in range(N):
                for j in range(N):
                    # 1. 주 대각선 -> 가운데 열
                    if j == mid:
                        ans[i][j] = board[i][i]

                    # 2. 가운데 열 -> 부 대각선
                    elif i+j == N-1:
                        ans[i][j] = board[i][mid]

                    # 3. 부 대각선 -> 가운데 행
                    elif i == mid:
                        ans[i][j] = board[N-j-1][j]

                    # 4. 가운데 행 -> 주 대각선
                    elif i == j:
                        ans[i][j] = board[mid][j]

                    else:
                        ans[i][j] = board[i][j]

            board = deepcopy(ans)

        for k in ans:
            print(*k)
```
