```python
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        dist = board[i][j]
        if dist == 0:
            continue

        if j + dist < n:
            dp[i][j + dist] += dp[i][j]

        if i + dist < n:
            dp[i + dist][j] += dp[i][j]

print(dp[n - 1][n - 1])

```
