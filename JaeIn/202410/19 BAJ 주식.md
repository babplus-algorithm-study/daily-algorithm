```python
import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cnt = int(input())
    arr = list(map(int, input().split()))

    max_num = 0
    result = 0
    for i in range(cnt -1  , -1 , -1):
        if arr[i] > max_num:
            max_num = arr[i]
        else:
            result += max_num - arr[i]

    print(result)

```
