```python
def solution(sequence, k):
    start = 0
    current_sum = 0
    min_length = float('inf')
    answer = []

    for end in range(len(sequence)):
        current_sum += sequence[end]

        while current_sum > k:
            current_sum -= sequence[start]
            start += 1


        if current_sum == k:
            current_length = end - start + 1
            if current_length < min_length:
                min_length = current_length
                answer = [start , end]

    return answer
```
