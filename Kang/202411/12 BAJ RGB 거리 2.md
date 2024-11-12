```python
import sys
input = lambda: sys.stdin.readline().rstrip()
MAX_INT = sys.maxsize

N = int(input())
graph = [list(map(int, input().split()) for _ in range(N))]

dp = [[0, 0, 0] for _ in range(N)]

dp[0] = graph[1]
for i in range(3):
    dp[0] = graph[0][:]
    dp[0][i] = MAX_INT
    for x in range(1, N):
        # 나머지 구현 이따가 쉴때~

print(min(dp[N - 1]))
```