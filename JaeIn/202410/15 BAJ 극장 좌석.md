```python
n = int(input())
v = int(input())
v_s = [int(input()) for _ in range(v)]

arr = [i for i in range(1 , n + 1)]
result = 1
dp = [0 for _ in range(42)]
dp[0] = 1
dp[1] = 1
dp[2] = 2


for i in range(3 , n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]


prev = 0
for i in v_s:
    result *= dp[i - 1 - prev]
    prev = i

result *= dp[n - prev]

print(result)





```
