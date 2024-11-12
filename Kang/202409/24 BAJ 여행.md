```python
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 1 
for _ in range(K):
    a, b, c = map(int, input().rstrip().split())
    if a < b:
        graph[a].append((b, c))
    
for i in range(1, N):
    for z in range(M):
        if dp[i][z] > 0:
            for (b, c) in graph[i]:
                dp[b][z + 1] = max(dp[b][z + 1], dp[i][z] + c)

max_count = 0

for k in dp[N]:
    max_count = max(k, max_count)
    
print(max_count - 1)
```