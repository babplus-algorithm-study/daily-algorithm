```python
def solution(storey):
    answer = 0

    while storey:
        remain = storey % 10

        # 6 ~ 9
        if remain >= 6:
            answer += 10 - remain
            storey += 10
        # 5
        elif remain == 5:
            if (storey // 10) % 10 >= 5:
                storey += 10
            answer += remain
        # 0 ~ 4
        else:
            answer += remain

        storey //= 10

    return answer
```
