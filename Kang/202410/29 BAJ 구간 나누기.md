```python
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

S = [0 for _ in range(N)]
dp = [[0] + [-3276800] * (M) for _ in range(N)]
number = [0 for _ in range(N)]
for i in range(0, N):
    num = int(input())
    number[i] = num
    if i == 0:
        S[i] = num
    else:
        S[i] = S[i - 1] + num

dp[0][1] = S[0]
one_max = S[0]

pp = [0 for _ in range(N)] # j = 1 일때를 초기화 하기 위해 사용하는 dp
pp[0] = S[0]

for i in range(1, N):
    if pp[i - 1] < 0:
        pp[i] = number[i]
    else:
        pp[i] = pp[i - 1] + number[i]
    one_max = max(one_max, pp[i])
    dp[i][1] = one_max

for i in range(0, N):
    for j in range(2, M + 1):
        if i >= (j * 2 - 2):
            dp[i][j] = dp[i - 1][j]
            for k in range(0, i - 1):
                dp[i][j] = max(dp[i][j], dp[k][j - 1] + S[i] - S[k + 1])

print(dp[N - 1][M])
```