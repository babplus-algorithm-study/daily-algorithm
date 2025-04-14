```python
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [0]

    for i in range(1, n):
        while stack and numbers[stack[-1]] < numbers[i]:
            print(stack)
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

```
