```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999999)

def dfs(cur , w):

    if w > m:
        return -9999999

    if cur == n:
        return 0

    if dp[cur][w] != -1:
        return dp[cur][w]


    dp[cur][w] = max(dfs(cur + 1 , w + item[cur][0]) + item[cur][1] , dfs(cur + 1 , w))

    return dp[cur][w]



n , m = map(int , input().split())
item = [list(map(int , input().split())) for _ in range(n)]

dp = [[-1 for _ in range(100001)]  for _ in range(n)]
ans = dfs(0 , 0)
print(ans)

```
