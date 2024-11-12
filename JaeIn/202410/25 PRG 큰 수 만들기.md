```python
def solution(number, k):
    answer = ''
    stack = []
    remove = 0

    for n in number:
        while stack and stack[-1] < n and remove < k:
            stack.pop()
            remove += 1
        stack.append(n)

    if remove < k:
        stack = stack[: -k - remove]
    return ''.join(stack)
```
