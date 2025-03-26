```python
from itertools import combinations
def solution(n, q, ans):
    possible_code = list(combinations(range(1, n + 1), 5))
    total_cnt = 0

    for code in possible_code:
        make_code = True
        for i in range(len(q)):
            if len(set(code) & set(q[i])) != ans[i]:
                make_code = False
                break

        if make_code:
            total_cnt += 1

    return total_cnt
```
