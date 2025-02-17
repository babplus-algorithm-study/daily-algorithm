```python
def solution(weights):
    answer = 0
    same = 0

    for i in range(len(weights)):
        for j in range(len(weights)):
            if i == j:
                continue
            if weights[i] * 2 == weights[j] * 2:
                same += 1
            elif weights[i] * 2 == weights[j] * 3:
                answer+= 1
            elif weights[i] * 3 == weights[j] * 4:
                answer += 1
            elif weights[i] * 2 == weights[j] * 4:
                answer+= 1

    result = (same/2) + answer
    return result
```
