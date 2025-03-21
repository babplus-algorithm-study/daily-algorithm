```python
N , M = map(int , input().split())

weight = []
for _ in range(N):
    weight.append(list(map(int , input().split())))

dp = [[0] * M for _ in range(N)]

for i in range(M):
    dp[0][i] = weight[0][i] + dp[0][i - 1]


for i in range(1 , N):
    temp1 = [0] * M
    temp2 = [0] * M

    for j in range(M):
        if j == 0:
            temp1[j] = weight[i][j] + dp[i - 1][j]
            temp2[M - 1 - j] = weight[i][M - 1 - j] + dp[i - 1][M - 1 - j]
            continue

        temp1[j] = weight[i][j] + max(dp[i - 1][j] , temp1[j - 1])
        temp2[M - 1 - j] = weight[i][M - 1 - j] + max(dp[i - 1][M - 1- j] , temp2[M - j])


    for m in range(M):
        dp[i][m] = max(temp1[m] , temp2[m])


print(dp[N - 1][M - 1])

```
