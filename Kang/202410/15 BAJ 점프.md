```python
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dp = [(10000000, 0) for _ in range(N)]
dp[1] = (1, 1) # 점프 횟수, x 값

out = set()
for _ in range(M):
    out_rock = int(input().rstrip())
    out.add(out_rock - 1)

for i in range(2, N):
    if i in out:
        continue
    for z in range(1, i):
        if z in out:
            continue
        if z + (dp[z][1] + 1) == i:
            if dp[z][0] + 1 <= dp[i][0]\
            and dp[z][1] + 1 > dp[i][1]:
                dp[i] = (dp[z][0] + 1, dp[z][1] + 1)
        if z + dp[z][1] == i:
            if dp[z][0] + 1 <= dp[i][0]\
            and dp[z][1] > dp[i][1]:
                dp[i] = (dp[z][0] + 1, dp[z][1])
        if dp[z][1] > 1\
        and z + (dp[z][1] - 1) == i:
            if dp[z][0] + 1 <= dp[i][0]\
            and dp[z][1] - 1 > dp[i][1]:
                dp[i] = (dp[z][0] + 1, dp[z][1] - 1)
        
if dp[N - 1][0] == 10000000:
    print(-1)
else:
    print(dp[N - 1][0])

```