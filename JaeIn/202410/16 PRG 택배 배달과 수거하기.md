```python
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pick = 0

    for d in range(len(deliveries) - 1 , -1, -1):
        deliver += deliveries[d]
        pick += pickups[d]

        while deliver > 0 or pick > 0:
            deliver -= cap
            pick -= cap
            answer += ((d + 1) * 2)
    return answer
```
