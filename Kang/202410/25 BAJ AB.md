```python
import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
cur_K = 0
last_idx = -1
a_count = 0
S = ['B' for _ in range(N)]
while cur_K < K:
    if last_idx <= a_count - 1:
        ch_idx = N - 1 - (a_count + 1)
        if S[ch_idx] == 'A':
            break
        S[ch_idx] = 'A'
        cur_K += 1
        last_idx = ch_idx
        a_count += 1
    else:
        S[last_idx] = 'B'
        last_idx -= 1
        S[last_idx] = 'A'
        cur_K += 1

if cur_K == K:
    print("".join(S))
else:
    print(-1)
```