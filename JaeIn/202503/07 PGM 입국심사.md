```python
def solution(n, times):
    answer = 0

    s = 1
    e = max(times) * n

    while s <= e:
        mid = (s + e) // 2

        people = 0
        for t in times:
            people += mid // t

            if people >= n:
                break

        if people >= n:
            answer = mid
            e = mid - 1
        else:
            s = mid + 1

    return answer
```
