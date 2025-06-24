```python
from collections import Counter


def solution(weights):
    answer = 0

    # 1:1
    counter = Counter(weights)
    for key , value in counter.items():
        if value >= 2:
            answer += value * (value - 1) / 2

    weights = set(weights)
    print(counter)

    #2:3, 2:4, 3:4
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]


    return answer
```
