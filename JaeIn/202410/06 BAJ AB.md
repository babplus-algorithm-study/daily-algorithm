```python
N, K = map(int, input().split())

ans = -1
s = ["B"] * N
total = 0
a_count = 0

for i in range(N):
    s[N - 1] = 'A'
    total -= a_count
    a_count += 1
    for j in range(N - 1 , i , -1):
        if total == K: break
        s[j] , s[j - 1] = s[j - 1] , s[j]
        total += 1

    if total == K: break

print(''.join(s) if total == K else -1)
```
